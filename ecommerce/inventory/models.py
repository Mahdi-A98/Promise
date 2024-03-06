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
