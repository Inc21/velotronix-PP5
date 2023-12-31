# Generated by Django 4.2.6 on 2023-11-10 23:45

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='product_images/noimage.webp', force_format='WEBP', keep_meta=True, null=True, quality=85, scale=None, size=[500, 400], upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=85, scale=None, size=[500, 400], upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=85, scale=None, size=[500, 400], upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=85, scale=None, size=[500, 400], upload_to='product_images/'),
        ),
    ]
