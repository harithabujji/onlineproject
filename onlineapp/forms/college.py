from onlineapp.models import *
from django import forms

class Addcollege(forms.ModelForm):
    class Meta:
        model=College
        exclude={'id'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'location'}),
            'acronym':forms.TextInput(attrs={'class':'form-control','placeholder':'acronym'}),
            'contact':forms.EmailInput(attrs={'class':'form-control','placeholder':'contact'})
        }
