from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product

SPAM_WORDS = {"казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"}


class CatalogForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image"]

    def __init__(self, *args, **kwargs):
        super(CatalogForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'description'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'укажите описание'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'image'
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'укажите фото продукта'
        })

        # Настройка атрибутов виджета для поля 'category'
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'укажите категорию'
        })

        # Настройка атрибутов виджета для поля 'price'
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену'  # Текст подсказки внутри поля
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name and any(spam in name.lower() for spam in SPAM_WORDS):
            raise ValidationError({"name": "Наименование не может содержать спам‑слова"})

        if description and any(spam in description.lower() for spam in SPAM_WORDS):
            raise ValidationError({"description": "Описание не может содержать спам‑слова"})

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        print(f"DEBUG: price value={price}, type={type(price)}")
        if price <= 0:
            raise ValidationError("Стоимость не должна быть отрицательной или нулевой")
        return price
