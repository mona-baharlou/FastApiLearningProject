import asyncio
from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

server = "localhost"
database = "BlogDB"
driver = "ODBC Driver 17 for SQL Server"
sqlserver_async_url = (
    f"mssql+aioodbc://@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}&trusted_connection=yes"
)


# sqlserver_url = (f"mssql+pyodbc://@{server}/{database}?driver={
# driver.replace(' ', '+')}&trusted_connection=yes")


engine = create_async_engine(sqlserver_async_url, echo=True)


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


class Base(DeclarativeBase, MappedAsDataclass):
    pass

# Base = declarative_base()


@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


