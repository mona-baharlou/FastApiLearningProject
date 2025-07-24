from fastapi import APIRouter

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


