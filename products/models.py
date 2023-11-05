# pylint: disable=missing-docstring
from django.db import models


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
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
