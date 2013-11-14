# coding=utf-8
"""Admin pages for our models."""
from django.contrib import admin

# Register your models here.
from models import Scribble, ScribbleType


class ScribbleAdmin(admin.ModelAdmin):
    """Admin interface for scribbles."""
    list_display = ('name', 'scribble_date')
    list_filter = ('name', 'scribble_date')
    search_fields = ('name',)


class ScribbleTypeAdmin(admin.ModelAdmin):
    """Admin interface for scribbles."""
    search_fields = ('name',)

#Register each model with its associated admin class
admin.site.register(Scribble, ScribbleAdmin)
admin.site.register(ScribbleType, ScribbleTypeAdmin)
