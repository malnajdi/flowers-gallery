from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import asyncio
from django.http import HttpResponse
from django.views import View

from extra_views import ModelFormSetView

from .models import Flower
from .forms import FlowerForm, FlowerUpdateForm

    
class HomeView(ListView):
    template_name = 'home.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by = 3
    queryset = Flower.with_images.all()


class FlowerDetailView(DetailView):
    template_name = 'detail.html'
    model = Flower
    context_object_name = 'flower'


class FlowerCreateView(LoginRequiredMixin, PermissionRequiredMixin, ModelFormSetView):
    model = Flower
    template_name = "create_flower.html"
    form_class = FlowerForm
    success_url = '/'
    login_url = '/accounts/login/'
    permission_required = 'gallery.add_flower'


    def formset_valid(self, formset):
        obj = []

        self.object_list = formset.save(commit=False)
        for object in self.object_list:
            object.user = self.request.user
            obj.append(object)
            object.save()
        return HttpResponseRedirect(self.get_success_url())



class FlowerUpdateView(LoginRequiredMixin, UpdateView):
    model = Flower
    template_name = "update_flower.html"
    form_class = FlowerUpdateForm
    success_url = '/'
    login_url = '/accounts/login/'


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


class FlowerDeleteView(LoginRequiredMixin, DeleteView):
    model = Flower
    template_name = "delete_flower.html"
    form_class = FlowerForm
    success_url = '/'
    login_url = '/accounts/login/'


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform view logic using await.
        result = []
        async for flower in Flower.objects.all():
            result.append(flower)

        flower = await Flower.objects.filter(user__username='malnajdi').afirst()

        return render(request, "index.html", {"results": result, "flower": flower})