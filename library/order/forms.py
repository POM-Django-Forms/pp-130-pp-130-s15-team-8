from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'plated_end_at']
        widgets = {
            'plated_end_at': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            )
        }
        labels = {
            'book': 'Книга',
            'plated_end_at': 'Планове повернення'
        }


