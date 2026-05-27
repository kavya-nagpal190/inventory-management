from inventory.models import Product,Sales
from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = "__all__"
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError('price cannot be less than 0')
        return value
    def validate_quantity(self,value):
        if value<=0:
            raise serializers.ValidationError('quantity cannot be less than 0')
        return value
 

class SalesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Sales
        fields = "__all__"
    
    def validate_quantity_sold(self,value):
        if value<=0:
            raise serializers.ValidationError('quantity cannot be less than 0')
        return value
    def create(self, validated_data):
        with transaction.atomic():
            quantity = validated_data['quantity_sold']
            product = validated_data['product_sold']
            if product.quantity < quantity:
             raise serializers.ValidationError('Not Enough Stock..')
            product.quantity -=quantity
            product.save()
            return super().create(validated_data)

        
        