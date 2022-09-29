from rest_framework import serializers
from app.models import User, Firm, Product, Transaction


class FirmSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120, allow_blank=True)
    class Meta:
        model = Firm
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120, allow_blank=True)
    email = serializers.CharField(max_length=120, allow_blank=True)
    firm = FirmSerializer()
    class Meta:
        model = User
        fields = ['id','name', 'email', 'firm']

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120, allow_blank=True)
    price = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ['id','name', 'price']

class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total = serializers.IntegerField()
    user = UserSerializer()
    class Meta:
        model = Transaction
        fields = ['id', 'product', 'total', 'user']

