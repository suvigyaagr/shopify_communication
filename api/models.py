from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    vendor = models.CharField(max_length=100, null=False, blank=False)
    product_type = models.CharField(max_length=100, null=True, blank=True)
    handle = models.CharField(max_length=100)
    published_scope = models.CharField(max_length=30)
    tags = models.CharField(max_length=200, blank=True, null=True)
    admin_graphql_api_id = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    published_at = models.DateTimeField()


class WeightUnits:
    KG = "kg"
    LB = "lb"


class CurrencyUnits:
    USD = "USD"
    INR = "INR"


class Variant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    currency = models.CharField(max_length=10, default=CurrencyUnits.USD)
    sku = models.CharField(max_length=30, null=True, blank=True)
    position = models.IntegerField()
    inventory_policy = models.CharField(max_length=30)
    fulfillment_service = models.CharField(max_length=30)
    option1 = models.CharField(max_length=30, null=True, blank=True)
    option2 = models.CharField(max_length=30, null=True, blank=True)
    option3 = models.CharField(max_length=30, null=True, blank=True)
    image_id = models.CharField(max_length=100, null=True, blank=True)
    taxable = models.BooleanField()
    barcode = models.CharField(max_length=30, null=True, blank=True)
    grams = models.DecimalField(decimal_places=2, max_digits=8)
    weight = models.DecimalField(decimal_places=2, max_digits=8)
    weight_unit = models.CharField(max_length=10, default=WeightUnits.KG)
    inventory_item_id = models.CharField(max_length=30)
    inventory_quantity = models.IntegerField()
    old_inventory_quantity = models.IntegerField()

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

