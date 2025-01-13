from django.contrib import admin
from django.urls import path
from products.views import ProductView, basket_add, ProductsList, ProductsCategoryList

urlpatterns = [
    path("<int:product_id>/", ProductView.as_view(), name="product-detail"),
    path("baskets/add/<int:product_id>/", basket_add, name="basket_add"),
    path("all-prods/", ProductsList.as_view(), name="all-prods"),
    path("cat/<slug:category_slug>", ProductsCategoryList.as_view(), name="category"),
]