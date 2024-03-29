from django.contrib import admin
from .models import (
    Product, ProductType, ProductInventory,
    Category, Brand, Stock, Media,
    ProductAttributeValues, ProductTypeAttribute
    )
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductTypeAttribute)