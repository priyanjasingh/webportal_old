from django import forms
from models import contacts

class contactForm(forms.ModelForm):
    username = forms.CharField()
   

    class Meta:
        model = contacts
        fields = ['username']
