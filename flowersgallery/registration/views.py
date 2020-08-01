from django.views.generic import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login/'
