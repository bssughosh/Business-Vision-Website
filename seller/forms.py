from django import forms
from .models import ProductData
from django.utils.translation import ugettext_lazy as _
import string


class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = ProductData
        fields = ('p_name', 'p_img', 'p_price', 'min_q', 'p_desc')
        labels = {
            'p_name': _('Enter Product Name'),
            'p_img': _('Provide Image of Product'),
            'p_price': _('Enter Product Price'),
            'min_q': _('Enter Minimum quantity to be purchased'),
            'p_desc': _('Enter Product Description'),
        }
        widgets = {
            # 'p_name': forms.TextInput(
            #     attrs={
            #         'class': 'inp',
            #     }
            # ),
            'p_price': forms.TextInput(
                attrs={
                    'class': 'form-control inp',
                }
            ),
            'min_q': forms.TextInput(
                attrs={
                    'class': 'form-control inp',
                }
            ),
            'p_dec': forms.Textarea(
                attrs={
                    'class': 'form-control inp1',
                }
            ),
        }

    def clean(self):
        super(ProductUploadForm, self).clean()
        p_price = str(self.cleaned_data.get('p_price'))
        min_q = str(self.cleaned_data.get('min_q'))

        if not p_price.isdigit():
            self._errors['p_price'] = self.error_class(['Enter only numeric values'])

        if not min_q.isdigit():
            self._errors['min_q'] = self.error_class(['Enter only numeric values'])

        return self.cleaned_data
