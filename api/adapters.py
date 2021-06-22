import json
import requests
from django.conf import settings


class ShopifyAdminApiAdapter:
    def __init__(self):
        self.base_url = f'https://{settings.SHOPIFY_API_KEY}:{settings.SHOPIFY_PASSWORD}@{settings.SHOPIFY_STORE}.myshopify.com/admin/api'

    def get_products(self):
        url = f'{self.base_url}/2021-01/products.json'
        request = requests.get(
            url=url,
        )
        return self.return_response(request)

    def create_order(self, items):
        url = f'{self.base_url}/2021-01/orders.json'
        body = {
            "order": {
                "line_items": items
            }
        }
        print(url)
        print(body)
        request = requests.post(
            url=url,
            json=body,
        )
        return self.return_response(request)

    def return_response(self, request):
        response_body = json.loads(request.text)
        print(request.status_code, response_body)
        return request.status_code, response_body
