from typing import Protocol

from sqlalchemy import select

from falinks.database import AsyncSessionLocal
from falinks.model.user import User


class GetActiveUsersFunc(Protocol):
    async def __call__(self) -> list[User]:
        ...


async def get_active_users() -> list[User]:
    query = select(User).where(User.active == None).order_by(User.id)
    async with AsyncSessionLocal() as session:
        result = await session.execute(query)
        return result.scalars().all()
