from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect
from gallery.models import Flower
from .models import Action


class LikeFlowerView(CreateView, UpdateView):
    http_method_names = ['post']
    model = Action
    success_url = '/'
    fields = ('liked', )

    def get_object(self, queryset=None):
        return Action.objects.get_or_create(
            user=self.request.user,
            flower=Flower.objects.get(
                id=self.kwargs.get('flower_id')
            )
        )[0]

    def _like_or_dislike(self):
        if self.request.POST.get('like'):
            return True
        
        if self.request.POST.get('dislike'):
            return False

        return None

    def form_valid(self, form):
        interaction = self.get_object()
        interaction.liked = self._like_or_dislike()
        interaction.save()
        return HttpResponseRedirect(self.success_url)
    