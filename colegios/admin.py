from django.contrib import admin
from .models import Colegio

@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'corporacion')
    list_filter  = ('corporacion',)
    search_fields = ('nombre',)

