from sys import prefix
from typing import Annotated

import uvicorn
from fastapi import Body, Depends, FastAPI
from pydantic import BaseModel

from db import Base, engine
from routers.users import router as user_router

app = FastAPI()


@app.on_event("startup")  # check alembic for migration
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router, prefix="/users")

# if __name__ == "__main__":
# uvicorn.run(app)