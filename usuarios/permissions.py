# backend/usuarios/permissions.py

from rest_framework.permissions import BasePermission


class EsAdmin(BasePermission):
    """
    Permite sólo a usuarios con rol 'admin'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'admin')


class EsCliente(BasePermission):
    """
    Permite sólo a usuarios con rol 'cliente'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'cliente')


class EsProfesor(BasePermission):
    """
    Permite sólo a usuarios con rol 'profesor'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'profesor')


class EsCoordinador(BasePermission):
    """
    Permite sólo a usuarios con rol 'coordinador'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'coordinador')


class EsContadora(BasePermission):
    """
    Permite sólo a usuarios con rol 'contadora'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'contadora')


class EsAdminOCliente(BasePermission):
    """
    Permite acceso si el usuario es admin O cliente.
    """
    def has_permission(self, request, view):
        return EsAdmin().has_permission(request, view) or EsCliente().has_permission(request, view)


class EsAdminOCoordinador(BasePermission):
    """
    Permite acceso si el usuario es admin O coordinador.
    """
    def has_permission(self, request, view):
        return EsAdmin().has_permission(request, view) or EsCoordinador().has_permission(request, view)


# Opcional: Permite Admin, Coordinador o Profesor
class EsAdminOCoordinadorOProfesor(BasePermission):
    """
    Permite acceso si el usuario es admin, coordinador o profesor.
    """
    def has_permission(self, request, view):
        return (
            EsAdmin().has_permission(request, view)
            or EsCoordinador().has_permission(request, view)
            or EsProfesor().has_permission(request, view)
        )


class EsProfesor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.rol == 'profesor')
