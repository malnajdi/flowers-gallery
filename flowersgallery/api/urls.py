from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('flowers/', views.FlowerListAPIView.as_view()),
    path('flowers/<int:id>/', views.FlowerDetailAPIView.as_view()),
]