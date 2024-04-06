# In the name of GOD
from django.urls import path

from .views import (
    CategoryListView,
    ProductListView,
    ProductByCategory,
    ProductInventoryByWebId,
    ProductDetail
)


urlpatterns = [

    path("inventory/category/all/", CategoryListView.as_view()),
    path("inventory/product/all/", ProductListView.as_view()),
    path("inventory/products/category/<str:category>/", ProductByCategory.as_view()),
    path("inventory/<int:web_id>/", ProductInventoryByWebId.as_view()),
    path("inventory/<slug:category_slug>/<slug:product_slug>", ProductDetail.as_view()),
]
