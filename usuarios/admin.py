# backend/usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'rol', 'is_staff', 'is_active'
    )
    list_filter = ('rol', 'is_staff', 'is_active')
    # Añadimos el campo `rol` a los formularios de edición y creación
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rol',)}),
    )
