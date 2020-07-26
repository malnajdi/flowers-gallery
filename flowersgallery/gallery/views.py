from django.views.generic import View, TemplateView
# from django.shortcuts import render


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'home.html')
    
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, *kwargs)
        context.update({
            'counter': 11
        })
        return context