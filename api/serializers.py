from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.models import Product, Variant


class ShopifyVariantsSerializer(serializers.ModelSerializer):
    # product_id = SerializerMethodField()

    class Meta:
        model = Variant
        fields = (
            "id",
            "product_id",
            "title",
            "price",
            "currency",
            "sku",
            "position",
            "inventory_policy",
            "fulfillment_service",
            "option1",
            "option2",
            "option3",
            "option3",
            "image_id",
            "taxable",
            "barcode",
            "grams",
            "weight",
            "weight_unit",
            "inventory_item_id",
            "inventory_quantity",
            "old_inventory_quantity",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        product_id = self.context.get("product_id")
        variant, created = Variant.objects.get_or_create(
            id=validated_data['id'], product_id=product_id,
            defaults=validated_data
        )
        return variant


class ShopifyProductsSerializer(serializers.ModelSerializer):
    variants = ShopifyVariantsSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "vendor",
            "product_type",
            "handle",
            "published_scope",
            "tags",
            "admin_graphql_api_id",
            "created_at",
            "updated_at",
            "published_at",
            "variants",
        )

    def create(self, validated_data):
        print('Inside ShopifyProductsSerializer create')
        variants = validated_data.pop("variants")
        product, created = Product.objects.get_or_create(id=validated_data['id'], defaults=validated_data)
        for variant in variants:
            serializer = ShopifyVariantsSerializer(data=variant, context={'product_id': product.id})
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        return product
