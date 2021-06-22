from api.controllers import ShopifyGetProductsController


def fetch_shopify_produts():
    ShopifyGetProductsController().process()
