from django.shortcuts import render
from django.views.generic.detail import DetailView

from products.models import Products


class ProductView(DetailView):
    model = Products
    template_name = 'products/single_product_variable.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = context['product'].color.all()
        context['sizes'] = context['product'].size.all()
        return context

