from django.shortcuts import render
from django.views.generic.detail import DetailView

from products.models import Products, ProductImages, Review


class ProductView(DetailView):
    model = Products
    template_name = 'products/single_product_variable.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['colors'] = context['product'].color.all()
        context['sizes'] = context['product'].size.all()
        context['images'] = ProductImages.objects.filter(product_id=context['product'].id)
        context['reviews'] = Review.objects.filter(product_id=context['product'].id)
        context['reviews_count'] = context['reviews'].count()
        context['avarage_points'] = context['reviews'].avarage_points()


        return context

