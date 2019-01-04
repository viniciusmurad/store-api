from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serialiazers import CategorySerializer
from .models import Category

class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

