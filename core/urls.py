# backend/core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de autenticación
    path('api/auth/', include('usuarios.auth_urls')),

    # Usuarios (incluye coordinadores, contadoras, profesores)
    path('api/usuarios/', include('usuarios.urls')),

    # Otras apps
    path('api/corporaciones/', include('corporaciones.urls')),
    path('api/colegios/', include('colegios.urls')),
    path('api/cursos/', include('cursos.urls')),
    path('api/talleres/', include('talleres.urls')),
    path('api/asistencias/', include('asistencias.urls')),
]
