from django import forms
from .models import ProductData

class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = ProductData
        fields = ('Name', 'Image', )