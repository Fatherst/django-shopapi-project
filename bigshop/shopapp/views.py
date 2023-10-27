from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .models import Product, Category
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView

# @api_view()
# def index_view(request:Request)->Response:
#     print('f')
#     return Response(Product.objects.all())


class ListProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self,request: Request)->Response:
        images = {"images":[{'src':'','alt':''}]}
        return Response(images)


class ListCategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer