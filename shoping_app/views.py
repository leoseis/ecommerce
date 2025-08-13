from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import DetailedProductSerializer, ProductSerializer
from rest_framework.response import Response
from .models import Product



@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = DetailedProductSerializer(product)
    return Response(serializer.data)


# Create your views here.
