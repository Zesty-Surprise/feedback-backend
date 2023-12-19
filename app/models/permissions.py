from datetime import datetime, timedelta
from typing import Annotated

from fastapi import  Depends, HTTPException, status
from app.api.api_v1.controllers.auth import get_current_user
from .user import User
from ..core.config import role_permissions

class PermissionChecker:
    def getUserPermissions(self, user: User):
        for permission in role_permissions:
            if permission["role"] == user["role"]:
                return permission["permissions"]

    def __init__(self, required_permissions: list[str]):
        self.required_permissions = required_permissions

    def __call__(self, user: User = Depends(get_current_user)):      
        
        response_object = {}
        user_perms = self.getUserPermissions(user)
        filter = None

        for r_perm in self.required_permissions:
        
            if r_perm not in user_perms:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Forbidden'
                )
            
            for permission in role_permissions:
                if user["role"] == permission["role"]:
                    filter = permission['filter']

            if filter is not None:
                response_object = {
                    "authorized": True,
                    "permissions":user_perms,
                    "filter": filter
                }
            else:
                response_object = {
                    "authorized": True,
                    "permissions":user_perms,
                    "filter": None
                }
            
        return response_object
