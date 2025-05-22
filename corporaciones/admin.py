# backend/corporaciones/admin.py

from django.contrib import admin
from .models import Corporacion

@admin.register(Corporacion)
class CorporacionAdmin(admin.ModelAdmin):
    list_display    = ('nombre', 'rut', 'coordinador')
    list_filter     = ('coordinador',)
    search_fields   = ('nombre', 'rut')
    filter_horizontal = ('contadoras',)

