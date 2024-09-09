from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """
    Разрешает доступ:
    - только авторизованным пользователям для GET и DELETE запросов,
    - только неавторизованным пользователям для POST запросов.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return not request.user.is_authenticated
        elif request.method in ['GET', 'DELETE']:
            return request.user.is_authenticated
        return False
