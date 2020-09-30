from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """ Class to determine if a user is owner of a booking. """
    pass
