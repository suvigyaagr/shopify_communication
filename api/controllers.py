from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import status

from api.adapters import ShopifyAdminApiAdapter
from api.exceptions import ShopifyProductAdditionException
from api.models import OrderItem, Product
from api.serializers import ShopifyProductsSerializer, ShopifyCreateOrderSerializer


class ListProductsController:
    def __init__(self, request):
        self.request = request
        self.params = request.GET
        self.response = None
        self.api_response_status = None
        print("ListProductsController init")

    def process(self):
        limit = self.params.get("limit", 10)
        page = int(self.params.get("page", 1))
        products_list = Product.objects.all()
        paginator = Paginator(products_list, limit)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            products = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            products = paginator.page(paginator.num_pages)

        serialized_products = []
        for product in products:
            serializer = ShopifyProductsSerializer(product)
            serialized_products.append(serializer.data)

        self.response = {
            "count": paginator.count,
            "current_page": page,
            "total_pages": paginator.num_pages,
            "products": serialized_products,
        }
        return self.response, status.HTTP_200_OK


class ShopifyGetProductsController:
    def __init__(self, request):
        self.request = request
        self.products = []
        self.api_response = None
        self.api_response_status = None
        print("ShopifyGetProductsController init")

    def process(self):
        self.api_response_status, self.api_response = ShopifyAdminApiAdapter().get_products()
        if self.api_response and "products" in self.api_response:
            self.products = self.api_response.get("products", [])
        for product in self.products:
            print(product)
            serializer = ShopifyProductsSerializer(data=product)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

        return {"message": "Successful"}, self.api_response_status


class ShopifyCreateOrderController:
    def __init__(self, request):
        self.request = request
        self.order_item = None
        self.items = []
        self.api_response = None
        self.api_response_status = None
        print("ShopifyCreateOrderController init")

    def _process_input(self):
        body = self.request.data
        variant_id = body.get('variant_id')
        quantity = body.get('quantity')
        self.items = [
            {
                "variant_id": variant_id,
                "quantity": quantity,
            }
        ]
        self.order_item = OrderItem.objects.create(variant_id=variant_id, quantity=quantity)
        print(self.items)
        print(self.order_item)

    def process(self):
        self._process_input()
        self.api_response_status, self.api_response = ShopifyAdminApiAdapter().create_order(self.items)
        if self.api_response_status == status.HTTP_201_CREATED:
            order_details = self.api_response.get("order")
            serializer = ShopifyCreateOrderSerializer(data=order_details, context={"order_item": self.order_item})
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

        return self.api_response, self.api_response_status
