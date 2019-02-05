from django.forms import ModelForm

from .models import Product, Customers


class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'manufacturer', 'price', 'image']


class ProductBuyForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number']
