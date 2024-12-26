from django.contrib import admin
from products.models import ProductCategory, Products, Color, Size, ProductImages

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImages)