from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'price', 'image', 'description', 'buy_link']


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 1:
            raise forms.ValidationError("Price must be a positive value.")
        if price > 10000:
            raise forms.ValidationError("Price is too high, please enter a realistic value.")
        return price

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description