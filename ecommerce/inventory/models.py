from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from mptt.models import TreeForeignKey, MPTTModel

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(verbose_name=_("name"), max_length=100)
    slug = models.SlugField(verbose_name=_("slug"), max_length=150, unique=True)
    is_active = models.BooleanField(verbose_name=_("is active"), default=False)
    parent = TreeForeignKey(to="self", on_delete=models.PROTECT, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        db_table = "category"
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("name",)


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=150)
    slug = models.SlugField(max_length=255)
    web_id = models.CharField(max_length=50, unique=True)

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="product_images/", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}"
    
    def get_thumbnail(self):
        if self.thumbnail:
            return settings.BASE_URL + self.thumbnail.url
        else: 
            return ""
        
    # def make_tumbnail(self, image, size=(300, 200)):
    #     img = Image.open(image)
    #     img.convert("RGB")
    #     img.tumbnail(size)
        
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, "JPEG", quality=85)
        
    #     thumbnail = File(thumb_io, name=image.name)
    #     return thumbnail


class Brand(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True
    )

    class Meta:
        db_table = "brand"
        verbose_name = _("brand")
        verbose_name_plural = _("brands")

    def __str__(self):
        return self.name


class ProductAttributeCategory(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100)
    slug = models.SlugField(verbose_name=_("slug"), max_length=150, unique=True)
    is_active = models.BooleanField(verbose_name=_("is active"), default=False)
    class Meta:
        db_table = "product_attribute_category"
        verbose_name = _("product attribute category")
        verbose_name_plural = _("product attribute categories")


class ProductAttribute(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=250, unique=True)
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)
    category = models.ForeignKey(to=ProductAttributeCategory, null=True, blank=True, on_delete=models.SET_NULL)
    is_selective = models.BooleanField(_("is selective"), default=False)

    class Meta:
        verbose_name = _("attribute")
        verbose_name_plural = _("attributes")
    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=250)
    product_type_attributes = models.ManyToManyField(
        to=ProductAttribute,
        related_name="product_type_attributes",
        through="ProductTypeAttribute"
    )

    def __str__(self):
        return self.name


class ProductAttributeValueImage(models.Model):
    image = models.ImageField(upload_to="product_attribute_value_images/")
    alt_text = models.CharField(verbose_name=_("alternative text"), max_length=100, null=True, blank=True)
    defualt_width = models.PositiveSmallIntegerField(verbose_name=_("default width"), null=True, blank=True)
    defualt_height = models.PositiveSmallIntegerField(verbose_name=_("default height"), null=True, blank=True)
    default_border_radious = models.PositiveSmallIntegerField(verbose_name=_("default border radious"), null=True, blank=True)

    def get_image(self):
        return settings.BASE_URL + self.image.url
    
    def __str__(self) -> str:
        return f"{self.alt_text}"


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        on_delete=models.PROTECT,
        related_name="product_attribute"
    )
    attribute_value = models.CharField(
        verbose_name=_("attribute value"),
        max_length=250
    )
    attribute_value_image = models.ForeignKey(ProductAttributeValueImage, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _("attribute value")
        verbose_name_plural = _("attribute values")

    def __str__(self):
        return f"{self.product_attribute.name}: {self.attribute_value}"


class ProductInventory(models.Model):
    sku = models.CharField(
        verbose_name=_("sku"),
        max_length=20,
        unique=True
    )
    upc = models.CharField(
        max_length=12,
        unique=True
    )
    product_type = models.ForeignKey(
        to=ProductType,
        related_name="product_type",
        on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        to=Product,
        related_name="product",
        on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name=_("brand"),
        related_name="brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        verbose_name=_("attribute values"),
        through="ProductAttributeValues",
    )
    retail_price = models.PositiveBigIntegerField(
        verbose_name=_("retail price"),
    )
    store_price = models.PositiveBigIntegerField(
        verbose_name=_("store price"),
    )
    weight = models.FloatField(
        verbose_name=_("weight"),
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True
    )
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)
    is_deleted = models.BooleanField(verbose_name=_("is deleted"), default=False)
    is_default = models.BooleanField(verbose_name=_("is default"), default=False)
    is_digital = models.BooleanField(verbose_name=_("is digital"), default=False)

    class Meta:
        verbose_name = _("product inventory")
        verbose_name_plural = _("product inventories")

    def __str__(self):
        return self.sku


class Media(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        verbose_name=_("product inventory"),
        related_name="media",
        on_delete=models.PROTECT
    )
    img_url = models.ImageField(upload_to="product_inventory_images/")
    alt_text = models.CharField(
        verbose_name=_("alternative text"),
        max_length=255,
    )
    is_feature = models.BooleanField(
        verbose_name=_("is feature"),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )

    def __str__(self):
        return self.alt_text
    
    def get_image(self):
        if self.img_url:
            return settings.BASE_URL + self.img_url.url
        else:
            return ""

class Stock(models.Model):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        null=True,
        blank=True,
    )
    units = models.IntegerField(
        default=0,
    )
    units_sold = models.IntegerField(
        default=0,
    )


class ProductAttributeValues(models.Model):
    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevaluess",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevaluess",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("attributevalues", "productinventory"),)
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attributes")

    def __str__(self):
        return f"{self.productinventory.sku} - {self.attributevalues.product_attribute.name}"


class ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="productattribute",
        on_delete=models.PROTECT,
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name="producttype",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("product_attribute", "product_type"),)
