from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product

SPAM_WORDS = {"казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"}


class CatalogForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image"]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name and any(spam in name.lower() for spam in SPAM_WORDS):
            raise ValidationError({"name": "Name не может содержать спам‑слова"})

        if description and any(spam in description.lower() for spam in SPAM_WORDS):
            raise ValidationError({"description": "Description не может содержать спам‑слова"})

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        print(f"DEBUG: price value={price}, type={type(price)}")
        if price <= 0:
            raise ValidationError("Стоимость не должна быть отрицательной или нулевой")
        return price
