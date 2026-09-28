from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование категории", help_text="Веедите наименование категории"
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Веедите описание категории", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование продукта", help_text="Веедите наименование продукта"
    )
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(
        upload_to="products", blank=True, null=True, verbose_name="Фото", help_text="Загрузите фото продукта"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена за покупку", help_text="Введите цену за покупку"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name}: {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
