from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.HomeView.as_view(), name="flower-home"),
    path('flower/<int:pk>/', views.FlowerDetailView.as_view(), name='flower-detail'),
    path('flower/create/', views.FlowerCreateView.as_view(), name='flower-create'),
    path('flower/<int:pk>/update/', views.FlowerUpdateView.as_view(), name='flower-update'),
    path('flower/<int:pk>/delete/', views.FlowerDeleteView.as_view(), name='flower-delete'),
    
]