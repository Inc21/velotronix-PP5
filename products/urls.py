# pylint: disable=missing-docstring
from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path('product_admin/', views.product_admin, name='product_admin'),
    path("delete/<int:product_id>/", views.delete_product,
         name="delete_product"),
    path("unhide_product/<int:product_id>/", views.unhide_product,
         name="unhide_product"),
]
