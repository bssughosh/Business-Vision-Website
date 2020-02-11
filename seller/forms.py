from django import forms
from .models import ProductData
from django.utils.translation import ugettext_lazy as _


class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = ProductData
        fields = ('p_name', 'p_img', 'p_price', 'min_q',)
        labels = {
            'p_name': _('Enter Product Name'),
            'p_img': _('Provide Image of Product'),
            'p_price': _('Enter Product Price'),
            'min_q': _('Enter Minimum quantity to be purchased'),
        }
        widgets = {
            # 'p_name': forms.TextInput(
            #     attrs={
            #         'class': 'inp',
            #     }
            # ),
            'p_price': forms.TextInput(
                attrs={
                    'class': 'inp',
                }
            ),
            'min_q': forms.TextInput(
                attrs={
                    'class': 'inp',
                }
            ),
            'p_dec': forms.Textarea(
                attrs={
                    'class': 'inp',
                }
            ),
        }
