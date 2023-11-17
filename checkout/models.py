from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                        blank=True, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      blank=True, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      blank=True, null=True)
   
