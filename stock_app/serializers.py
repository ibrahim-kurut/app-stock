from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchases, Sales

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = '__all__'

class PurchasesSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    category = serializers.SerializerMethodField()

    class Meta:
        model = Purchases
        fields = '__all__'

    def get_category(self, obj):
        return obj.product.category.name

class SalesSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    product = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Sales
        fields = '__all__'
