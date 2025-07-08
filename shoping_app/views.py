from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Product



@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# Create your views here.
