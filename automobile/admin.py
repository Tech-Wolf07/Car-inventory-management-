from django.contrib import admin
from .models import Inventory, Expenses, Persons

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Expenses)
admin.site.register(Persons)
