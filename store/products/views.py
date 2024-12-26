from django.shortcuts import render
from django.views.generic.detail import DetailView

from products.models import Products


class ProductView(DetailView):
    model = Products
    template_name = 'products/single_product_variable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Products.objects.filter(pk=self.kwargs['pk'])
        print(context['product'])

