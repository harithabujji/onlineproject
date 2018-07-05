from django import forms
from onlineapp.models import *

class studentform(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','college']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'db_folder':forms.TextInput(attrs={'class':'form-control','placeholder':'db_folder'}),
            'dropped_out':forms.CheckboxInput(attrs={'class':'form-control','placeholder':'dropped-out'})
        }