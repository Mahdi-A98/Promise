from inventory.models import (
    Category, Product, ProductInventory, ProductType, ProductAttributeValue,
    ProductAttributeValues, Media, Stock, Brand
    )

from rest_framework import serializers
from django.conf import settings


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "web_id", "category", "description", "get_thumbnail", "get_absolute_url"]
        editable = False
        depth = 2


class ProductAttributeValueSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True

    def to_representation(self, instance):
        data = super().to_representation(instance)
        attribute_image = data["attribute_value_image"] or {}
        if attribute_image:
            data["attribute_value_image"]["get_image"] = settings.BASE_URL + attribute_image.get("image", "")
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "is_Active", "slug", "parent"]
        read_only = True


class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text", "is_feature"]
        read_only = True
        editable = False

        def get_img_url(self, obj):
            if obj.img_url:
                return obj.img_url.url
            else:
                return None


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = True


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["product_inventory", "alt_text", "is_feature", "img_url", "get_image"]


class ProductInventorySerializer(serializers.ModelSerializer):
    # media = ProductMediaSerializer(many=True, read_only=True)
    media = MediaSerializer(many=True)
    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(read_only=True)
    attributes = ProductAttributeValueSerializers(source="attribute_values", many=True, read_only=True)

    class Meta:
        model = ProductInventory
        depth = 2
        fields = [
            "sku",
            "upc",
            "product",
            "product_type",
            "brand",
            "store_price",
            "is_default",
            "weight",
            "attributes",
            # "promotion_price",
            "media"
        ]
        read_only = True

    def get_promotion_price(self, obj):
        # ToDo to implement Promotion model later
        return obj.store_price


class ProductInventorySearchSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "name",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand"
        ]
