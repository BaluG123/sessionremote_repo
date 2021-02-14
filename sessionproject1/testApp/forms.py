from django import forms

class name(forms.Form):
    name=forms.CharField()

class age(forms.Form):
    age=forms.IntegerField()

class gf(forms.Form):
    gfname=forms.CharField()    
