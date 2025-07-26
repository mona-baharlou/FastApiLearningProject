#from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_db
from operations.users import UserOperation
from schema._input import RegisterInput

router = APIRouter()


@router.post("/register")
async def register(
    db: AsyncSession = Depends(get_db),
    user: RegisterInput = Body()
   ):
    op = UserOperation(db)
    created_user = await op.create(username=user.username,
                                   password=user.password)
    return {"id": created_user.id, "username": created_user.username}


@router.post("/login")
async def login():
    ...


@router.get("/{username}/")
async def get_user_profile(
  username: str,
  db: AsyncSession = Depends(get_db),
):
    op = UserOperation(db)
    user_profile = await op.get_user_by_username(username=username)
    return user_profile




@router.put("/update")
async def update_user_profile():
    ...


# @router.get("/items")
# async def read_items(db: AsyncSessionLocal = Depends(get_db)):
# result = await db.execute(text("SELECT * FROM my_table"))
# rows = result.fetchall()
# return rows
