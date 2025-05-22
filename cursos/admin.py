from django.contrib import admin
from .models import Curso, Alumno

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'colegio')
    list_filter  = ('colegio',)
    search_fields = ('nombre',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso')
    list_filter  = ('curso',)
    search_fields = ('nombre',)
