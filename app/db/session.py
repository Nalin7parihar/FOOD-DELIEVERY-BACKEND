from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession


engine = create_async_engine(settings.DATABASE_URL,echo=True)

SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine,class_=AsyncSession)

Base = declarative_base()
async def get_db():
    async with SessionLocal() as session:
      yield session
      



