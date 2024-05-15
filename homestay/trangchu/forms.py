from django import forms
from .models import customer_info
class CustomerForm(forms.ModelForm):
    customer_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ten'}), required=False)
    customer_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}), required=False)
    customer_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}), required=False)



