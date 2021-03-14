from django import forms

from .models import Cake,Rate

class AddCakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['title','short_description','long_description','image']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['refer','content']

