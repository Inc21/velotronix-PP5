from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Product


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'added_date',
        'popularity',
        'image1',
        'image2',
        'image3',
        'image4',
    )

    ordering = ('-added_date', 'sku')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
