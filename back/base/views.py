from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

def index(req):
    return JsonResponse('hello', safe=False)

class products_view(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, category=None):  # Add 'category' parameter with a default value of None
        if category:
            return self.get_products_by_category(request, category)
        else:
            my_model = Product.objects.all()
            serializer = ProductSerializer(my_model, many=True)
            return Response(serializer.data)

    def post(self, request, category=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)  # Set the category field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_products_by_category(self, request, category):
        my_model = Product.objects.filter(category=category)
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)
