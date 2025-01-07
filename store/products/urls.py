from django.contrib import admin
from django.urls import path
from products.views import ProductView, basket_add

urlpatterns = [
    path("<int:product_id>/", ProductView.as_view(), name="product-detail"),
    path("baskets/add/<int:product_id>/", basket_add, name="basket_add"),
]