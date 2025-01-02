from django.contrib import admin
from django.urls import path
from products.views import ProductView

urlpatterns = [
    path("<int:post_id>/", ProductView.as_view(), name="product-detail"),
]