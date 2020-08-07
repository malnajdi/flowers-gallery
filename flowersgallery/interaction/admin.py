from django.contrib import admin
from .models import Action


class ActionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Action, ActionAdmin)