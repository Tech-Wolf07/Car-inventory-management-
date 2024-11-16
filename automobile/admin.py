from django.contrib import admin
from .models import Inventory, Expensens, Persons

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Expensens)
admin.site.register(Persons)
