from django.contrib import admin
from products.models import ProductCategory, Products, Color, Size, ProductImages, Review, Sex, TypeOfProduct

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImages)
admin.site.register(Review)
admin.site.register(Sex)
admin.site.register(TypeOfProduct)
