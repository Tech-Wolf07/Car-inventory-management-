from django.db import models, transaction
from django.db.models.signals import post_save, post_delete

class Inventory(models.Model):
    car_name = models.CharField(max_length=20)
    colour = models.CharField(max_length=20, blank=True, null=True)
    no_of_owner = models.IntegerField(blank=True, null=True)
    kms_driven = models.IntegerField(blank=True, null=True)
    passing_till = models.DateField(blank=True, null=True)
    insuarance_till = models.DateField(blank=True, null=True)
    plate_no = models.CharField(max_length=15, unique=True, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('sale', 'For Sale'), ('buy', 'For Buy')])
    year = models.DateField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    profit = models.IntegerField(default=0)
    

class Expenses(models.Model):
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    amount = models.BigIntegerField(null=True,blank=True)
    image_URL = models.ImageField(blank=True, null=True)


class Persons(models.Model):
    name = models.CharField(max_length=20)
    mob_no = models.IntegerField()
    address = models.CharField(max_length=50)
    p_type = models.CharField(max_length=10, choices=[('customer', 'Customer'), ('dealer', 'Dealer')], default='customer')
