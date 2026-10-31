from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from .forms import CatalogForm
from .models import Product, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .services import get_products_from_cache_by_category


# Create your views here.
class ProductsListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class CategoriesListView(ListView):
    model = Category
    template_name = "catalog/categories_list.html"
    context_object_name = "categories"
    ordering = ["name"]


class CategoryProductsListView(ListView):
    template_name = "catalog/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        self.category = get_object_or_404(Category, id=category_id)
        return get_products_from_cache_by_category(category_id)


# @method_decorator(cache_page(60 * 5), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CatalogForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = CatalogForm
    template_name = "catalog/product_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        is_owner = obj.owner == self.request.user
        is_super = self.request.user.is_superuser
        has_change_perm = self.request.user.has_perm("catalog.can_unpublish_product")
        if not (is_owner or is_super or has_change_perm):
            raise PermissionDenied
        return obj

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        is_owner = obj.owner == self.request.user
        is_super = self.request.user.is_superuser
        has_delete_perm = self.request.user.has_perm("catalog.delete_product")
        if not (is_owner or is_super or has_delete_perm):
            raise PermissionDenied
        return obj


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductTogglePublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        has_perm = request.user.has_perm("catalog.can_unpublish_product")

        if not has_perm:
            raise PermissionDenied

        product.is_published = not product.is_published
        product.save(update_fields=["is_published"])

        return redirect("catalog:product_detail", pk=product.pk)
