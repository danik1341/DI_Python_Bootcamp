from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE']:
            return obj.administrator == request.user