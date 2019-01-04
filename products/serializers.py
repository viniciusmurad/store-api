from rest_framework import serializers
from .models import Product, ProductCategory
from stores.models import Store
from categories.models import Category
from stores.serializers import StoreSerializer
from categories.serialiazers import CategorySerializer
class ProductSerializer(serializers.ModelSerializer):

    store = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'store', 'category')

    def get_store(self, obj):
        store = Store.objects.get(id=obj.store_id)
        return StoreSerializer(store).data

    def get_category(self, obj):
        categories = []
        c = ProductCategory.objects.filter(product_id=obj.id).values_list('category_id', flat=True)
        for i in c:
            category = Category.objects.get(id=i)
            categories.append(CategorySerializer(category).data)
        return categories
