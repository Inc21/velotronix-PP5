# Generated by Django 4.2.6 on 2023-11-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_full_name'),
        ('products', '0011_remove_product_image1_url_remove_product_image2_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorites', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
    ]