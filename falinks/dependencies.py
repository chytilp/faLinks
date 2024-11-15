from typing import Generator

from falinks.database import AsyncSessionLocal
from falinks.query.user import GetActiveUsersFunc, get_active_users


async def get_db() -> Generator[AsyncSessionLocal, None, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_active_users_factory() -> GetActiveUsersFunc:
    return get_active_users
