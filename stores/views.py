from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StoreSerializer
from .models import Store

class StoreList(APIView):

    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    def get(self, request, pk):
        store = Store.objects.get(pk=pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk):
        store = Store.objects.get(pk=pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = Store.objects.get(pk=pk)
        store.delete()
        return Response(status.HTTP_200_OK)