from django import forms

from .models import AddDetails


class AddDetailsForm(forms.ModelForm):
    username = forms.CharField()
    emailaddress = forms.EmailField()

    class Meta:
        model = AddDetails
        fields = ['emailaddress', 'username']
