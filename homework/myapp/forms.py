from django import forms
from .models import Products


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=60, label='Название продукта', widget=forms.TextInput(attrs={'class': 'input__form', 'required': True}))
    description = forms.CharField(max_length=200, label='Описание продукта', widget=forms.TextInput(attrs={'class': 'input__form', 'required': True}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Стоимость продукта', widget=forms.NumberInput(attrs={'class': 'input__form', 'required': True}))
    quantity = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={'class': 'input__form', 'required': True}))
    image = forms.ImageField(label='Добавтье изображение')

    class Meta:
        model = Products()
        fields = ['title', 'description', 'price', 'quantity', 'image']

