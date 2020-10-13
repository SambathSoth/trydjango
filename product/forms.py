from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "cols": 120}))
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
        # if "CFE" in title:
        #     return title
        # else:
        #     raise forms.ValidationError("This is not a validation title")

class RawProductForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "cols": 120}))
    price       = forms.DecimalField()
