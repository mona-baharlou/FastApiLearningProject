from fastapi import FastAPI

from db import Base, engine
from routers.users import router as user_router

app = FastAPI()


@app.on_event("startup")  # check alembic for migration
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router, prefix="/users")
