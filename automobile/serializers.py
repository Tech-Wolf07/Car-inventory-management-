# serializers.py
from rest_framework import serializers
from .models import Inventory, Expenses
from django.contrib.auth.models import User


class InventorySerializer(serializers.ModelSerializer):
    calculated_total_expenses = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # Read-only field

    class Meta:
        model = Inventory
        fields = '__all__'

    
class ExpensesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Expenses
        fields = ['id', 'inventory_id', 'title', 'description', 'amount', 'image_URL']


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    
    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('Username already exits.')
        
        if data['email']:
                if User.objects.filter(email = data['email']).exists():
                    raise serializers.ValidationError('email already exits.')
        
        return data
            
    def create(self, validated_data):
            user = User.objects.create(username = validated_data['username'], email = validated_data['email']) 
            user.set_password(validated_data['password'])
            user.save()
            return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



    