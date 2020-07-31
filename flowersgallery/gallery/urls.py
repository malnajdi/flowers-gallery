from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('flower/<int:pk>/', views.FlowerDetailView.as_view(), name='flower-detail')
]