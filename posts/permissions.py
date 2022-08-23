from rest_framework import permissions

""" Создается пользвоательское разрешение(расширяется метод от класса BasePermisson)"""


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # (SAFE METHOD включает GET, OPTIONS,HEAD)
            return True
        return obj.author == request.user  # в остальных случаях досутпен CRUD
