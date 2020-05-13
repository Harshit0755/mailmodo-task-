from django import forms
from .models import *
class Add_Album_form(forms.ModelForm):
    class Meta:
        model=Album
        exclude=("date",)
        widgets={
            "name":forms.TextInput(attrs={"placeholder":"Album", "required":""}),
            "artists":forms.TextInput(attrs={"placeholder": "Artist"}),
            "image": forms.FileInput(),
            "company": forms.TextInput(attrs={"placeholder": "Company"}),

        }