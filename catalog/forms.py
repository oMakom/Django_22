from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm, ImageField

from catalog.models import Product

SPAM_WORDS = {"казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"}

def validate_image_size(value):
    max_size = 5 * 1024 * 1024  # 5 МБ
    if value.size > max_size:
        raise ValidationError("Файл слишком большой. Максимальный размер: 5 МБ.")

class CatalogForm(ModelForm):
    image = ImageField(
        required=False,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpeg', 'png']),
            validate_image_size,
        ],
    )

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
