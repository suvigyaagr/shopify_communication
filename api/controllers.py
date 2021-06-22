from api.adapters import ShopifyAdminApiAdapter
from api.exceptions import ShopifyProductAdditionException
from api.serializers import ShopifyProductsSerializer


class ShopifyGetProductsController:
    def __init__(self, request):
        self.request = request
        self.products = []
        self.api_response = None
        print("ShopifyGetProductsController init")

    def process(self):
        self.api_response = ShopifyAdminApiAdapter().get_products()
        if "products" in self.api_response:
            self.products = self.api_response.get("products", [])
        print(f"products count={len(self.products)}")
        try:
            for product in self.products:
                print(product)
                serializer = ShopifyProductsSerializer(data=product)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    raise ShopifyProductAdditionException(serializer.errors)
        except ShopifyProductAdditionException as e:
            print(e)
            return {"message": "error"}

        return {"message": "Successful"}
