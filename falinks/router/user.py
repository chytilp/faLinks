from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from falinks.database import AsyncSessionLocal
from falinks.dependencies import get_db
from falinks.model.request import UserRequest
from falinks.model.response import UserResponse
from falinks.model.user import User

router = APIRouter()


@router.get("/users/", tags=["users"], response_model=list[UserResponse])
async def get_users(db: AsyncSessionLocal = Depends(get_db)):
    query = select(User).where(User.active == None).order_by(User.id)
    async with db as session:
        result = await session.execute(query)
        return result.scalars().all()


@router.get("/user", tags=["users"], response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSessionLocal = Depends(get_db)):
    query = (
        select(User)
        .where(User.id == user_id))
    async with db as session:
        users = await session.execute(query)
        return users.scalars().first()


@router.post("/users/", tags=["users"])
async def insert_user(user: UserRequest, db: AsyncSessionLocal = Depends(get_db)):
    db_user = User(**user.dict())
    async with db.begin():
        db.add(db_user)
        await db.flush()
        user_id: int = db_user.id
        await db.commit()
    return {"user_id": user_id}
