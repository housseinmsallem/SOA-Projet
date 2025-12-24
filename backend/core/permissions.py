from rest_framework.permissions import BasePermission


class IsAdministrateur(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.groups.filter(name="Administrateur").exists()
            or request.user.role == "ADM"
        )


class IsEmploye(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Employe").exists()
        )


class IsVeterinaire(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Veterinaire").exists()
        )


class IsResponsableProduction(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Responsable_Production").exists()
        )
