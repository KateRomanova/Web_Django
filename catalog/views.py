from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from catalog.models import Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Product.objects.all()[:5]
        return context


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:product_list')
