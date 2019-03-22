from django import forms
from app_00.models import Order
from app_00.models import Book

class OrderForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(),
                                  widget=forms.HiddenInput)
    class Meta:
        model  = Order
        fields = ('book', 'name', 'phone')

