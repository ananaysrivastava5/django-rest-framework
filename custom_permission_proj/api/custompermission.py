from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True   # permission allowed
        return False    #permission denied