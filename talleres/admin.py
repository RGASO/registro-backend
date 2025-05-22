from django.contrib import admin
from .models import Taller

@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso')
    list_filter  = ('curso',)
    search_fields = ('nombre',)
