from rest_framework import permissions


class RequestHasUserID(permissions.BasePermission):
    message = "Request must provide user_id"

    def has_permission(self, request, view):
        user_id = request.META.get("USER_ID")
        return True
        # if user_id:
        #     return True
        # return False