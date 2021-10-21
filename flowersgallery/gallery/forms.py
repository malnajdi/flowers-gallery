from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField()

    