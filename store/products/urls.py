from django.contrib import admin
from django.urls import path
from products.views import ProductView

urlpatterns = [
    path("<int:pk>/", ProductView.as_view(), name="product-detail"),
]