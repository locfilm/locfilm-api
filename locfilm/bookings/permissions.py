
from rest_framework import permissions

from locfilm.users.models import User

import random

class IsOwner(permissions.BasePermission):
    """
    Only person who assigned has permission
    """
    message = 'You are not host of this booking'
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user_id == request.user.id:
           return True
        else:
           return False

class IsAllowed(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)


    def has_object_permission(self, request, view, obj):
        print(obj)
        return random.choice([True, False])


class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
  #  def has_permission(self, request, view):
  #      return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # obj here is a UserProfile instance
        return False
