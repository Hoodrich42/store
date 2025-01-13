from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from products.models import Product, ProductImages, Review, Basket


class ProductView(DetailView):
    model = Product
    template_name = 'products/single_product_variable.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = context['product'].color.all()
        context['sizes'] = context['product'].size.all()
        context['images'] = ProductImages.objects.filter(product_id=context['product'].id)
        context['reviews'] = Review.objects.filter(product_id=context['product'].id)
        context['reviews_count'] = context['reviews'].count()
        context['avarage_points'] = context['reviews'].avarage_points()
        context['related_cats'] = context['product'].get_type()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        context['related_prods'] = []
        for cat in context['related_cats']:
            context['related_prods'] += Product.objects.filter(category_id=cat.id)
        return context


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class ProductsList(ListView):
    model = Product
    paginate_by = 30
    context_object_name = 'products'
    template_name = 'products/home_clean.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsCategoryList(ListView):
    model = Product
    paginate_by = 30
    slug_url_kwarg = 'category_slug'
    context_object_name = 'products'
    template_name = 'products/home_clean.html'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

