# In the name of GOD

from django.db.models import Count
from .models import ProductAttribute, ProductAttributeValue

def mark_selective_attributes():
    selective_atrributes_ids = list(
        ProductAttributeValue.objects.all()
        .values('product_attribute')
        .annotate(values_count=Count('product_attribute'))
        .filter(values_count__gt=1)
        .values_list('product_attribute_id', flat=True)
    )
    ProductAttribute.objects.filter(id__in=selective_atrributes_ids).update(is_selective=True)