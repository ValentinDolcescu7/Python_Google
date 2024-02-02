from django import forms
from django.contrib import sessions 
from django.core.validators import MinValueValidator

class QuoteForm(forms.Form):
    symbol = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mx-auto w-auto mb-3',
                'autofocus': True,
                'placeholder': 'Symbol'
            }
        ),
        label="",
    )


class BuySellForm(QuoteForm):
    shares = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mx-auto w-auto mb-3',
                'min': '1',
                'placeholder': 'Shares'
            }
        ),
        validators=[MinValueValidator(1)],
        label="",
    )
    