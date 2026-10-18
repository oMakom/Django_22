from django.forms import forms

from catalog.models import Product


class CatalogForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price','category', 'image']
