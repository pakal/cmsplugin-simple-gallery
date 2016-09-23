# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleGalleryPointer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(choices=[(b'cmsplugin_simple_gallery/fancy_image.html', 'Display first only image form gallery'), (b'cmsplugin_simple_gallery/fancy_gallery.html', 'Display all images from gallery')], default=b'cmsplugin_simple_gallery/fancy_image.html', max_length=255)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsplugin_simple_gallery.SimpleGallery')),
            ],
            options={
                'verbose_name': 'SimpleGallery',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SimpleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inline_ordering_position', models.IntegerField(blank=True, null=True)),
                ('src', models.ImageField(height_field=b'src_height', upload_to=b'cmsplugin_simple_gallery/images', width_field=b'src_width')),
                ('src_height', models.PositiveSmallIntegerField(editable=False, null=True)),
                ('src_width', models.PositiveSmallIntegerField(editable=False, null=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsplugin_simple_gallery.SimpleGallery')),
            ],
            options={
                'ordering': ('inline_ordering_position',),
                'abstract': False,
            },
        ),
    ]
