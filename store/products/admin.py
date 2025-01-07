from django.contrib import admin
from products.models import ProductCategory, Product, Color, Size, ProductImages, Review, Sex, TypeOfProduct, Basket

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImages)
admin.site.register(Review)
admin.site.register(Sex)
admin.site.register(TypeOfProduct)
admin.site.register(Basket)
