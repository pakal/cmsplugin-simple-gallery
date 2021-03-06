from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable
from easy_thumbnails.files import get_thumbnailer
import easy_thumbnails.utils
from .settings import *

class SimpleGallery(models.Model):

    class Meta:
        verbose_name_plural = "Simple Galleries"
        
    name = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.name

class SimpleImage(Orderable):
    gallery = models.ForeignKey(SimpleGallery)
    src = models.ImageField(upload_to=CMS_SIMPLEGALLERY_UPLOAD_TO,
        height_field='src_height', width_field='src_width')
    src_height = models.PositiveSmallIntegerField(editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(editable=False, null=True)

    def save(self):
        super(SimpleImage, self).save()
        get_thumbnailer(self.src).get_thumbnail(CMS_SIMPLEGALLERY_THUMBNAIL_OPTIONS)

    def get_thumbnail(self):
        thumbnailer = get_thumbnailer(self.src)
        thb = thumbnailer.get_thumbnail(CMS_SIMPLEGALLERY_THUMBNAIL_OPTIONS, save=True)
        return thb.url

    def __unicode__(self):
        return str(self.pk)

class SimpleGalleryPointer(CMSPlugin):
    gallery = models.ForeignKey(SimpleGallery)
    template = models.CharField(max_length=255, choices=CMS_SIMPLEGALLERY_TEMPLATES,
        default=CMS_SIMPLEGALLERY_DEFAULT_TEMPLATE, editable=len(CMS_SIMPLEGALLERY_TEMPLATES) > 1)
    class Meta:
        verbose_name = _("SimpleGallery")

    def __unicode__(self):
        return _('%(count)d image(s) in gallery') % {'count': self.gallery.simpleimage_set.count()}

