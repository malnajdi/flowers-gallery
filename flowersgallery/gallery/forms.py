from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Flower


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = '__all__'
        labels = {
            'description': _('Tell us about yourself'),
        }
        help_texts = {
            'description': _('Some useful help text.'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 1, 'rows': 1}),
        }
