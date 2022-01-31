from fastapi import Depends

from fief.db import AsyncSession
from fief.dependencies.account import get_current_account_session
from fief.managers import (
    AuthorizationCodeManager,
    ClientManager,
    RefreshTokenManager,
    TenantManager,
    get_manager,
)


async def get_tenant_manager(
    session: AsyncSession = Depends(get_current_account_session),
) -> TenantManager:
    return get_manager(TenantManager, session)


async def get_client_manager(
    session: AsyncSession = Depends(get_current_account_session),
) -> ClientManager:
    return get_manager(ClientManager, session)


async def get_authorization_code_manager(
    session: AsyncSession = Depends(get_current_account_session),
) -> AuthorizationCodeManager:
    return get_manager(AuthorizationCodeManager, session)


async def get_refresh_token_manager(
    session: AsyncSession = Depends(get_current_account_session),
) -> RefreshTokenManager:
    return get_manager(RefreshTokenManager, session)
