# inventory/forms.py  

from django import forms  
from .models import Product, Supplier, SaleOrder  

class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = ['name', 'email', 'phone', 'address']  

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = ['name', 'description', 'category', 'price', 'stock_quantity', 'supplier']  

class SaleOrderForm(forms.ModelForm):  
    class Meta:  
        model = SaleOrder  
        fields = ['product', 'quantity']
