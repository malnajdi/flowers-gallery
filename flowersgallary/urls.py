from django.contrib import admin
from django.urls import path
from .views import WelcomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view()),
]
