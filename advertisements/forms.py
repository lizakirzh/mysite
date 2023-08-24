from django import forms

class AdvertisementForm (forms. Form): 
    title = forms.CharField (max_length=80)
    description = forms.CharField()
    price = forms.DecimalField()
    auction = forms.BooleanField()
    image = forms. ImageField()