# serializers.py
from rest_framework import serializers
from .models import Inventory, Expenses

class InventorySerializer(serializers.ModelSerializer):
    calculated_total_expenses = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # Read-only field

    class Meta:
        model = Inventory
        fields = '__all__'

    
class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id', 'inventory_id', 'title', 'description', 'amount', 'image_URL']



