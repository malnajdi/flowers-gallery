from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Flower
from .forms import FlowerForm

    
class HomeView(ListView):
    template_name = 'home.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by = 2


class FlowerDetailView(DetailView):
    template_name = 'detail.html'
    model = Flower
    context_object_name = 'flower'


class FlowerCreateView(CreateView):
    model = Flower
    template_name = "create_flower.html"
    form_class = FlowerForm
    success_url = '/'


class FlowerUpdateView(UpdateView):
    model = Flower
    template_name = "update_flower.html"
    form_class = FlowerForm
    success_url = '/'


class FlowerDeleteView(DeleteView):
    model = Flower
    template_name = "delete_flower.html"
    form_class = FlowerForm
    success_url = '/'