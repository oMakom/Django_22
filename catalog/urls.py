from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductsListView, ProductDetailView, ContactTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="home"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
