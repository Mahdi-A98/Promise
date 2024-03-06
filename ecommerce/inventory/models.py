from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import TreeForeignKey

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=100
    )
    slug = models.SlugField(
        verbose_name=_("slug"),
        max_length=150,
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=False
    )
    parent = TreeForeignKey(
        to="self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        db_table = "category"
        verbose_name = _("category")
        verbose_name_plural = _("category's")


class Product(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=150,
    )
    slug = models.SlugField(
        max_length=255,
    )
    web_id = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name