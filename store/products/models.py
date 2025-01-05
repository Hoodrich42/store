from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=255, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    size = models.ManyToManyField(to=Size)
    color = models.ManyToManyField(to=Color)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Товар: {self.name} | Категория: {self.category.name}'


class ProductImages(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')

    def count_images(self):
        count = ProductImages.objects.filter(product_id=self.product.id).count()
        if count >= 5:
            raise ValidationError(f'Можно добавить не более 5 изображений')

    def save(self, *args, **kwargs):
        self.count_images()
        super(ProductImages, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товара'

    def __str__(self):
        return f'Картинка для {self.product.name}'


class Rewiew(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    points = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отзыв товара'
        verbose_name_plural = 'Отзывы товара'

    def __str__(self):
        return f'Отзыв для товара: {self.product.name} | Оценка: {self.points}'


