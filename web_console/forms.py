from django import forms
from .models import *

class ProductUploadForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['productCode','productName', 'product','instock','sold','sale','price','description','images','image']
        # fields = '__all__' , use all the fields
