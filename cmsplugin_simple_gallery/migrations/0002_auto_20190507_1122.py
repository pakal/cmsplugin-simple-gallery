# Generated by Django 2.1.8 on 2019-05-07 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_simple_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simplegallery',
            options={'verbose_name_plural': 'Simple Galleries'},
        ),
        migrations.AlterField(
            model_name='simplegallerypointer',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_simple_gallery_simplegallerypointer', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='simplegallerypointer',
            name='template',
            field=models.CharField(choices=[('cmsplugin_simple_gallery/fancy_image.html', 'Display first only image form gallery'), ('cmsplugin_simple_gallery/fancy_gallery.html', 'Display all images from gallery')], default='cmsplugin_simple_gallery/fancy_image.html', max_length=255),
        ),
        migrations.AlterField(
            model_name='simpleimage',
            name='src',
            field=models.ImageField(height_field='src_height', upload_to='cmsplugin_simple_gallery/images', width_field='src_width'),
        ),
    ]
