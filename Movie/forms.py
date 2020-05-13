from django import forms
from .models import *


class Add_Movie_form(forms.ModelForm):
    class Meta:
        model = MovieDetails
        exclude=()
        widgets = {
            "cat":forms.Select(attrs={"width":"250px"}),
            "title":forms.TextInput(attrs={"placeholder":"Title"}),
            "duration":forms.TextInput(attrs={"placeholder":"Duration"}),
            "director":forms.TextInput(attrs={"placeholder":"Director"}),
            "description":forms.TextInput(attrs={"placeholder":"Description"}),
            "rating":forms.TextInput(attrs={"placeholder":"rating"}),
            "release_date":forms.DateInput(attrs={"placeholder":"release date"}),
            "img1":forms.FileInput(),
            "img2":forms.FileInput(),
            "img3":forms.FileInput(),
            "trailer":forms.TextInput(attrs={"placeholder":"Company"}),
            "producer":forms.TextInput(attrs={"placeholder":"Company"}),
        }

class Add_Starcast_form(forms.ModelForm):
    class Meta:
        model = StarCast
        exclude=()
        widgets = {
            "movie":forms.Select(attrs={"width":"250px"}),
            "name":forms.TextInput(attrs={"placeholder":"name"}),
            "photo":forms.FileInput(),
            "role_as":forms.TextInput(attrs={"placeholder":"role"}),
        }