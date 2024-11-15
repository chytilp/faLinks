from fastapi import APIRouter, Depends
from sqlalchemy import select

from falinks.database import AsyncSessionLocal
from falinks.dependencies import get_db
from falinks.model.request import RoleRequest
from falinks.model.response import RoleResponse
from falinks.model.user import Role

router = APIRouter()


@router.get("/roles/", tags=["roles"], response_model=list[RoleResponse])
async def get_roles(db: AsyncSessionLocal = Depends(get_db)):
    query = select(Role).where(Role.active==None).order_by(Role.id)
    async with db as session:
        result = await session.execute(query)
        return result.scalars().all()


@router.get("/role", tags=["roles"], response_model=RoleResponse)
async def get_role(role_id: int, db: AsyncSessionLocal = Depends(get_db)):
    query = (
        select(Role)
        .where(Role.id == role_id))
    async with db as session:
        roles = await session.execute(query)
        return roles.scalars().first()


@router.post("/roles/", tags=["roles"])
async def insert_role(role: RoleRequest, db: AsyncSessionLocal = Depends(get_db)):
    db_role = Role(**role.dict())
    async with db.begin():
        db.add(db_role)
        await db.flush()
        role_id: int = db_role.id
        await db.commit()
    return {"role_id": role_id}
