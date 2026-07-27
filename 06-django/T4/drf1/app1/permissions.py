from rest_framework.permissions import BasePermission

class isADMINReadonly(BasePermission):
  def has_permission(self,request,view):

    if request.methos in ["GET","HEAD","OPTION"]:
      return True
    return request.user.is_staff