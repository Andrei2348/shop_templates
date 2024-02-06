from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=60, label='Название продукта', widget=forms.TextInput(attrs={'class': 'input__form'}))
    description = forms.CharField(max_length=200, label='Описание продукта', widget=forms.TextInput(attrs={'class': 'input__form'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Стоимость продукта', widget=forms.NumberInput(attrs={'class': 'input__form'}))
    quantity = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={'class': 'input__form'}))

