from unittest import mock

from django.conf import settings
from django.test import TestCase
from rest_framework import status

from api.adapters import ShopifyAdminApiAdapter

TEST_SHOPIFY_API_KEY = 'abc'
TEST_SHOPIFY_PASSWORD = 'def'
TEST_SHOPIFY_STORE = 'def'


class ShopifyAdapterTestCase(TestCase):
    def test_correct_base_url(self):
        test_url = f'https://{settings.SHOPIFY_API_KEY}:{settings.SHOPIFY_PASSWORD}@{settings.SHOPIFY_STORE}.myshopify.com/admin/api'
        adapter = ShopifyAdminApiAdapter()
        self.assertEqual(adapter.base_url, test_url)

    @mock.patch('api.adapters.settings.SHOPIFY_API_KEY', TEST_SHOPIFY_API_KEY)
    @mock.patch('api.adapters.settings.SHOPIFY_PASSWORD', TEST_SHOPIFY_PASSWORD)
    @mock.patch('api.adapters.settings.SHOPIFY_STORE', TEST_SHOPIFY_STORE)
    def test_mock_base_url(self):
        test_url = f'https://{TEST_SHOPIFY_API_KEY}:{TEST_SHOPIFY_PASSWORD}@{TEST_SHOPIFY_STORE}.myshopify.com/admin/api'
        adapter = ShopifyAdminApiAdapter()
        self.assertEqual(adapter.base_url, test_url)

    @mock.patch('api.adapters.settings.SHOPIFY_API_KEY', TEST_SHOPIFY_API_KEY)
    def test_fetch_products_wrong_api_key(self):
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.get_products()
        self.assertEqual(status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("errors", response)

    @mock.patch('api.adapters.settings.SHOPIFY_PASSWORD', TEST_SHOPIFY_PASSWORD)
    def test_fetch_products_wrong_password(self):
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.get_products()
        self.assertEqual(status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("errors", response)

    @mock.patch('api.adapters.settings.SHOPIFY_STORE', TEST_SHOPIFY_STORE)
    def test_fetch_products_wrong_store(self):
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.get_products()
        self.assertEqual(status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("errors", response)

    @mock.patch('api.adapters.settings.SHOPIFY_API_KEY', TEST_SHOPIFY_API_KEY)
    def test_create_order_wrong_api_key(self):
        test_items = [
            {
                "variant_id": 32328252129347,
                "quantity": 2,
            }
        ]
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertEqual(status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("errors", response)

    @mock.patch('api.adapters.settings.SHOPIFY_PASSWORD', TEST_SHOPIFY_PASSWORD)
    def test_create_order_wrong_password(self):
        test_items = [
            {
                "variant_id": 32328252129347,
                "quantity": 2,
            }
        ]
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertEqual(status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("errors", response)

    @mock.patch('api.adapters.settings.SHOPIFY_STORE', TEST_SHOPIFY_STORE)
    def test_create_order_wrong_store(self):
        test_items = [
            {
                "variant_id": 32328252129347,
                "quantity": 2,
            }
        ]
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertEqual(status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("errors", response)

    def test_fetch_products_success(self):
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.get_products()
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertIn("products", response)

    def test_create_order_success(self):
        test_items = [
            {
                "variant_id": 32328252129347,
                "quantity": 2,
            }
        ]
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertEqual(status_code, status.HTTP_201_CREATED)
        self.assertIn("order", response)

    def test_create_order_invalid_input1(self):
        test_items = {}
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertNotEqual(status_code, status.HTTP_201_CREATED)
        self.assertIn("errors", response)

    def test_create_order_invalid_input2(self):
        test_items = []
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertNotEqual(status_code, status.HTTP_201_CREATED)
        self.assertIn("errors", response)

    def test_create_order_invalid_input3(self):
        test_items = {
            "variant_id": 32328252129347,
            "quantity": 2,
        }
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertNotEqual(status_code, status.HTTP_201_CREATED)
        self.assertIn("errors", response)

    def test_create_order_invalid_input4(self):
        """
        Invalid varaint_id
        """
        test_items = [
            {
                "variant_id": 123,
                "quantity": 2,
            }
        ]
        adapter = ShopifyAdminApiAdapter()
        status_code, response = adapter.create_order(test_items)
        self.assertNotEqual(status_code, status.HTTP_201_CREATED)
        self.assertIn("errors", response)
