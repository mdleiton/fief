from pydantic import UUID4

from fief.schemas.generics import BaseModel, CreatedUpdatedAt
from fief.schemas.role import RoleEmbedded
from fief.schemas.user import UserRead


class UserRoleCreate(BaseModel):
    id: UUID4


class BaseUserRole(CreatedUpdatedAt):
    user_id: UUID4
    role_id: UUID4


class UserRole(BaseUserRole):
    role: RoleEmbedded


class UserRoleWithUser(BaseUserRole):
    user: UserRead