from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.adapters import ShopifyAdminApiAdapter
from api.controllers import ShopifyGetProductsController, ShopifyCreateOrderController
from api.serializers import ShopifyProductsSerializer


@api_view(['GET'])
def health_view(request):
    print("Health")
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def shopify_get_products_view(request):
    response, status_code = ShopifyGetProductsController(request).process()
    return Response(data=response, status=status_code)


@api_view(['POST'])
def shopify_create_order_view(request):
    response, status_code = ShopifyCreateOrderController(request).process()
    return Response(data=response, status=status_code)
