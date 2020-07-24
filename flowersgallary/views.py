from django.views.generic import View
from django.http import HttpResponse


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome Mohammed!!')