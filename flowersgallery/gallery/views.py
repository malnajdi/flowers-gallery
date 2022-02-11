from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Flower
from .forms import FlowerForm, FlowerUpdateForm

    
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
    form_class = FlowerUpdateForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     pass

    def get_context_data(self, *args, **kwargs):
        kwargs.update({
            'test': 'test'
        })
        return super().get_context_data(*args, **kwargs)


class FlowerDeleteView(DeleteView):
    model = Flower
    template_name = "delete_flower.html"
    form_class = FlowerForm
    success_url = '/'