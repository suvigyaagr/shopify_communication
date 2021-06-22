from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.adapters import ShopifyAdminApiAdapter
from api.controllers import ShopifyGetProductsController, ShopifyCreateOrderController, ListProductsController, \
    ListOrdersController
from api.serializers import ShopifyProductsSerializer


@api_view(['GET'])
def health_view(request):
    print("Health")
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def list_products(request):
    """
    params:
        -limit: to limit the number of responses per page
        -page: page_number

    """
    response, status_code = ListProductsController(request).process()
    return Response(response, status_code)


@api_view(['GET'])
def list_orders(request):
    """
        params:
            -from_date: in the format of yyyy-mm-dd
            -to_date: in the format of yyyy-mm-dd
            -limit: to limit the number of responses per page
            -page: page_number

    """
    response, status_code = ListOrdersController(request).process()
    return Response(response, status_code)


@api_view(['GET'])
def shopify_get_products_view(request):
    response, status_code = ShopifyGetProductsController().process()
    return Response(data=response, status=status_code)


@api_view(['POST'])
def shopify_create_order_view(request):
    """
        Json Body example:
        {"variant_id": 32328279359555, "quantity": 12}
    """
    response, status_code = ShopifyCreateOrderController(request).process()
    return Response(data=response, status=status_code)
