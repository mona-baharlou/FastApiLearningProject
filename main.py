from sys import prefix
from typing import Annotated

import uvicorn
from fastapi import Body, Depends, FastAPI
from pydantic import BaseModel

from routers.users import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users")

if __name__ == "__main__":
    uvicorn.run(app)