
from rest_framework import serializers
from ProductApp.models import Categories, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id',
                  'name',
                  'description',
                  'pic_url')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id',
                  'name',
                  'category',
                  'pic_url',
                  'price_value',
                  'price_currency',
                  'dimension_value',
                  'dimension_unit',
                  'created_at',
                  'description')