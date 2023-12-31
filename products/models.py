from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User


class Category(models.Model):
    """
    A category model to store all the products in the database
    """
    class Meta:
        verbose_name_plural = 'Categories'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class Product(models.Model):
    """
    A product model to store all the products in the database
    """
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    specs = models.TextField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=True, blank=True)
    image1 = ResizedImageField(size=[500, 400], upload_to='product_images/',
                               null=True, force_format='WEBP', quality=85,
                               blank=True,
                               default='product_images/noimage.webp')
    image2 = ResizedImageField(size=[500, 400], upload_to='product_images/',
                               null=True, force_format='WEBP', quality=85,
                               blank=True)
    image3 = ResizedImageField(size=[500, 400], upload_to='product_images/',
                               null=True, force_format='WEBP', quality=85,
                               blank=True)
    image4 = ResizedImageField(size=[500, 400], upload_to='product_images/',
                               null=True, force_format='WEBP', quality=85,
                               blank=True)
    popularity = models.IntegerField(default=0)
    favorites = models.ManyToManyField(User, related_name='favorites',
                                       blank=True, default=None)
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    hidden = models.BooleanField(default=False)

    def increment_popularity(self):
        self.popularity += 1
        self.save()

    def __str__(self):
        return str(self.name)
