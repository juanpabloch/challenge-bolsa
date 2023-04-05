from django import forms
from api.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        
        
class ProductsUpdateForm(forms.Form):
    # buy     = forms.DecimalField(max_digits=10, decimal_places=2)
    # sell    = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Products
        fields = ("buy", "sell")