from django.db import models

class Inventory(models.Model):
    cid = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=20)
    colour = models.CharField(max_length=20, default=None)
    no_of_owner = models.IntegerField(default=None)
    kms_driven = models.IntegerField(default=None)
    passing_till = models.DateField(default=None)
    insuarance_till = models.DateField(default=None)
    plate_no = models.CharField(unique=True,default=None)
    status = models.CharField(choices=[('sale','For Sale'),('buy','For Buy')])
    year = models.DateField(default=None)
    condition = models.TextField(default=None)
    total_expenses =models.CharField(default=0) 
    profit = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.car_name}'

class Expensens(models.Model):
    cid = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50,null=True)
    amount = models.BigIntegerField(default=0)
    image_URL = models.ImageField(null=True,blank=True)

class Persons(models.Model):
    name = models.CharField(max_length=20)
    mob_no = models.IntegerField()
    address = models.CharField(max_length=50)
    p_type = models.CharField(choices=[('customer','Customer'),('dealer','Dealer')],default=None)


