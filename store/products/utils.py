
from .models import ProductCategory, TypeOfProduct


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = TypeOfProduct.objects.all()
        return context
