from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product, ProductCategory
from stores.models import Store

class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        categories = request.data['category']
        store = Store.objects.get(id=request.data['store'])
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            res = serializer.save(store=store)
            for cat in categories:
                ProductCategory.objects.create(product_id=res.id, category_id=cat)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self, request, pk):
        store = Product.objects.get(pk=pk)
        serializer = ProductSerializer(store)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk):
        categories = request.data['category']
        store = Store.objects.get(id=request.data['store'])
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(store=store)
            product_categories = ProductCategory.objects.filter(product_id=product.id)
            for product_category in product_categories:
                product_category.delete()
            for category in categories:
                ProductCategory.objects.create(product_id=product.id, category_id=category)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status.HTTP_200_OK)
