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
        upload_to="catalog/photo", blank=True, null=True, verbose_name="Фото", help_text="Загрузите фото продукта"
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name="products")
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

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", help_text="Веедите ваше имя")
    email = models.EmailField(verbose_name="Почта", help_text="Веедите почту")
    message = models.TextField(verbose_name="Сообщение", help_text="Веедите ваше сообщение")

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["name"]
