from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm, ImageField
from django.forms.widgets import CheckboxInput
from django import forms

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
            FileExtensionValidator(allowed_extensions=["jpeg", "png"]),
            validate_image_size,
        ],
    )

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image", "is_published"]

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.owner = user
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(CatalogForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите наименование",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'description'
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "укажите описание",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'image'
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
            }
        )

        # Настройка атрибутов виджета для поля 'category'
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "укажите категорию"}  # Добавление CSS-класса для стилизации поля
        )

        # Настройка атрибутов виджета для поля 'price'
        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите цену",  # Текст подсказки внутри поля
            }
        )
        if self.user and self.user.has_perm("catalog.can_unpublish_product"):
            self.fields["is_published"].widget = CheckboxInput(attrs={"class": "form-check-input"})
            self.fields["is_published"].label = "Опубликовать продукт"
        else:
            self.fields.pop("is_published", None)

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
