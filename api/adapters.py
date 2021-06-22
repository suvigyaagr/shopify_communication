import json

import requests

SHOPIFY_BASE_API_URL = 'https://a38f4a6a8cb713fe2bebdbf3df331f54:3182dcd29ff6c3f6f2dd325ba99b4216@mishipaytestdevelopmentemptystore.myshopify.com'


class ShopifyAdminApiAdapter:
    def __init__(self):
        self.base_url = SHOPIFY_BASE_API_URL

    def get_products(self):
        try:
            request = requests.get(
                url=f'{self.base_url}/admin/api/2021-01/products.json',
            )
            if request.status_code == 200:
                response = json.loads(request.text)
                print(response)
                return response

        except Exception as e:
            print(e)
        return None

    def create_order(self):
        try:
            request = requests.post(
                url=f'{self.base_url}/admin/api/2021-01/products.json',
                json={
                    "order": {
                        "line_items": [
                            {
                                "variant_id": 32066662432835,
                                "quantity": 2
                            }
                        ]
                    }
                }
            )
            if request.status_code == 200:
                response = json.loads(request.text)
                print(response)
                return response

        except Exception as e:
            print(e)
        return None
