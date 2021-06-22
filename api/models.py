from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    channel_product_id = models.IntegerField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    body_html = models.TextField()
    vendor = models.CharField(max_length=100, null=False, blank=False)
    product_type = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    published_scope = models.CharField(max_length=30)
    tags = models.CharField(max_length=200)
    admin_graphql_api_id = models.CharField(max_length=200)
    channel_created_at = models.DateTimeField()
    channel_updated_at = models.DateTimeField()
    channel_published_at = models.DateTimeField()


class WeightUnits:
    LB = "lb"


class CurrencyUnits:
    USD = "USD"
    INR = "INR"


class Variant(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    channel_variant_id = models.IntegerField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField()
    currency = models.CharField(max_length=10, default=CurrencyUnits.USD)
    sku = models.CharField(max_length=30, unique=True, null=False, blank=False)
    position = models.IntegerField()
    inventory_policy = models.CharField(max_length=30)
    fulfillment_service = models.CharField(max_length=30)
    inventory_management = models.CharField(max_length=30)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    image_id = models.IntegerField()
    taxable = models.BooleanField()
    barcode = models.CharField(max_length=30)
    grams = models.DecimalField()
    weight = models.DecimalField()
    weight_unit = models.CharField(max_length=10, default=WeightUnits.LB)
    inventory_item_id = models.IntegerField()
    inventory_quantity = models.IntegerField()
    old_inventory_quantity = models.IntegerField()

    channel_created_at = models.DateTimeField()
    channel_updated_at = models.DateTimeField()
    channel_published_at = models.DateTimeField()

