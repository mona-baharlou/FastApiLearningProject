from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/register")
async def register():
    ...


@router.post("/login")
async def login():
    ...


@router.get("/")
async def get_user_profile():
    ...


@router.put("/register")
async def update_user_profile():
    ...


# @router.get("/items")
# async def read_items(db: AsyncSessionLocal = Depends(get_db)):
   # result = await db.execute(text("SELECT * FROM my_table"))
   # rows = result.fetchall()
   # return rows
