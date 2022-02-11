from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Flower


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        exclude = ['user', ]
        labels = {
            'description': _('Tell us about yourself'),
        }
        help_texts = {
            'description': _('Some useful help text.'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 1, 'rows': 1}),
        }


class FlowerUpdateForm(FlowerForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'flower' not in title:
            raise ValidationError(_('Your title does not contain the word flower!!'))
        return title

    # def clean(self):
    #     pass