from django.contrib import admin

# Register your models here.
from api.models import Product, Variant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass
