from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase

server = "localhost"
database = "BlogDB"
driver = "ODBC Driver 17 for SQL Server"
database_url = (
    f"mssql+aioodbc://@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}&trusted_connection=yes"
)


engine = create_async_engine(database_url, echo=True)


async def check_connection():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT SYSTEM_USER, GETDATE();"))
        rows = result.fetchall()
        for row in rows:
            print(
                "Connected as User:", row[0], "| Current SQL Server time:",
                row[1]
                )


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


# @asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
