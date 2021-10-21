from django.views.generic.edit import FormView
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Flower
from .forms import ContactUsForm

    
class HomeView(ListView):
    template_name = 'home.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by = 2


class FlowerDetailView(DetailView):
    template_name = 'detail.html'
    model = Flower
    context_object_name = 'flower'


class ContactUsView(FormView):
    template_name = "contact_us.html"
    form_class = ContactUsForm
    success_url = '/'

    def form_valid(self, form):
        print(form)
        print('form was submitted successfully...')
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     pass

