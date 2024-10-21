from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import Select

from fief.models import UserRole, User
from fief.repositories.base import BaseRepository, UUIDRepositoryMixin


class UserRoleRepository(BaseRepository[UserRole], UUIDRepositoryMixin[UserRole]):
    model = UserRole

    def get_by_user_statement(self, user: UUID4) -> Select:
        statement = (
            select(UserRole)
            .where(UserRole.user_id == user)
            .options(joinedload(UserRole.role))
        )
        return statement
    
    def get_by_role_statement(self, role: UUID4) -> Select:
        statement = (
            select(UserRole)
            .where(UserRole.role_id == role)
            .options(joinedload(UserRole.user).joinedload(User.tenant))
        )
        return statement

    async def get_by_role_and_user(self, user: UUID4, role: UUID4) -> UserRole | None:
        return await self.get_one_or_none(
            select(UserRole)
            .where(UserRole.user_id == user, UserRole.role_id == role)
            .options(joinedload(UserRole.role))
        )

    async def get_by_role(self, role: UUID4) -> list[UserRole]:
        return await self.list(select(UserRole).where(UserRole.role_id == role))
