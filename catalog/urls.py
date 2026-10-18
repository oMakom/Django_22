from django.urls import path
from catalog.apps import CatalogConfig
from .views import (
    ProductsListView,
    ProductDetailView,
    ContactTemplateView,
    ProductsCreateView,
    ProductsDeleteView,
    ProductsUpdateView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductsListView.as_view(), name="home"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductsCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductsUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductsDeleteView.as_view(), name="product_delete"),
]
