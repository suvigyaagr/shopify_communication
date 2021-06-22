class ShopifyBaseException(Exception):
    def __init__(self, message):
        super(ShopifyBaseException, self).__init__(message)


class ShopifyProductAdditionException(ShopifyBaseException):
    pass
