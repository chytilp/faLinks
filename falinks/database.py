import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Model(DeclarativeBase):
    pass


load_dotenv()


def get_engine() -> AsyncEngine:
    return create_async_engine(os.environ["DATABASE_URL"], echo=True)


AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine(), class_=AsyncSession)
