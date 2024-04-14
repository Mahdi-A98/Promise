from django.contrib import admin
from .models import (
    Product, ProductType, ProductInventory,
    Category, Brand, Stock, Media,
    ProductAttribute, ProductAttributeValue,
    ProductAttributeValues, ProductTypeAttribute,
    ProductAttributeCategory, ProductAttributeValueImage
    )
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductTypeAttribute)
admin.site.register(ProductAttributeValueImage)
admin.site.register(ProductAttributeCategory)