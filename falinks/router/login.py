import traceback

from fastapi import APIRouter, Depends

from falinks.database import AsyncSessionLocal
from falinks.dependencies import get_db
from falinks.model.request import UserRequest
from falinks.model.response import UserRegistration
from falinks.model.user import User

router = APIRouter()


@router.post("/register/", tags=["login"], response_model=list[UserRegistration])
async def register_user(user: UserRequest, db: AsyncSessionLocal = Depends(get_db)):
    try:
        db_user = User(**user.dict())
        async with db.begin():
            db.add(db_user)
            await db.flush()
            user_id: int = db_user.id
            await db.commit()
            return UserRegistration(
                user_id=user_id,
                message="User created successfully",
                success=True,
            )

    except Exception as err:
        print(f"Error in insert_user: {err}, {traceback.format_exc()}")
        return UserRegistration(
            message="User creation failed",
            success=False,
        )


@router.post("/login/", tags=["login"])
async def login_user(user: UserRequest, db: AsyncSessionLocal = Depends(get_db)):
    pass
