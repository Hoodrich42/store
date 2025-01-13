from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime as dt

from django.urls import reverse
from users.models import User


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


class Sex(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class TypeOfProduct(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey(to=TypeOfProduct, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=255, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    sex = models.ForeignKey(to=Sex, on_delete=models.CASCADE, blank=True)
    size = models.ManyToManyField(to=Size)
    color = models.ManyToManyField(to=Color)

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'product_id': self.id})

    def get_type(self):
        category_id = self.category.id
        type = ProductCategory.objects.get(id=category_id).type
        return ProductCategory.objects.filter(type=type)

    def get_img(self):
        return ProductImages.objects.filter(product_id=self.id)[0]

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Товар: {self.name} | Категория: {self.category.name}'



class ProductImages(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
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


class ReciewsQuerySet(models.QuerySet):

    def avarage_points(self):
        if len(self) > 0:
            return sum(review.points for review in self) / self.count()
        else:
            return 0


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    points = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = ReciewsQuerySet.as_manager()

    def date_create(self):
        date = self.created_timestamp
        return date.strftime('%d.%m.%Y')


    class Meta:
        verbose_name = 'Отзыв товара'
        verbose_name_plural = 'Отзывы товара'

    def __str__(self):
        return f'Отзыв для товара: {self.product.name} | Оценка: {self.points}'


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity


