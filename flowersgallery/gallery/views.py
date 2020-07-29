from django.views.generic import View, TemplateView, ListView
from .models import Flower

    
class HomeView(ListView):
    template_name = 'home.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by = 2
