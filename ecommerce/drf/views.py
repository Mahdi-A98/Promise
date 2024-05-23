from django.shortcuts import render
from inventory.models import ProductInventory, Product, Category
from .serializers import ProductSerializer, ProductInventorySerializer, CategorySerializer

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)


class ProductByCategory(APIView):

    def get(self, request, category=None):
        queryset = Product.objects.filter(category__slug=category)
        serializer = ProductSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductInventoryByWebId(APIView):

    def get(self, request, web_id=None):
        queryset = ProductInventory.objects.filter(product__web_id=web_id)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    serializer_class = ProductInventorySerializer
    queryset = ProductInventory.objects.filter(is_active=True)

    def get(self, request, category_slug, product_slug):

        query_set = self.queryset.filter(product__slug=product_slug)
        if not category_slug == "main":
            query_set = query_set.filter(
                product__category__slug=category_slug
            )
        serializer = self.serializer_class(instance=query_set, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)