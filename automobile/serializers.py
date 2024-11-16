# serializers.py
from rest_framework import serializers
from .models import Inventory, Expensens

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['car_name', 'colour', 'no_of_owner','kms_driven','passing_till','insuarance_till', 'plate_no', 'status', 'year','condition','total_expenses','profit']  

    def create(self, validated_data):
        return Inventory.objects.create(**validated_data)
    
class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expensens
        fields = ['cid','exp_name','description','total_amt']


