from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache_by_category(category_id: int):
    """Получает список продуктов по категори из кэша, или из БД при пустом Хэше"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    key = f"products_by_{category_id}"
    products = cache.get(key)

    if products is None:
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, timeout=300)

    return products
