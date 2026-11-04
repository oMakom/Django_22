from django.urls import path
from catalog.apps import CatalogConfig
from .views import (
    ProductsListView,
    ProductDetailView,
    ContactTemplateView,
    ProductsCreateView,
    ProductsDeleteView,
    ProductsUpdateView,
    ProductTogglePublishView,
    CategoryProductsListView,
    CategoriesListView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductsListView.as_view(), name="home"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("category/<int:category_id>/", CategoryProductsListView.as_view(), name="category_products"),
    path("categories/", CategoriesListView.as_view(), name="categories_list"),
    path("product/new/", ProductsCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductsUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductsDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/toggle-publish/", ProductTogglePublishView.as_view(), name="product_toggle_publish"),
]
