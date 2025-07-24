from typing import Annotated

import uvicorn
from fastapi import Body, Depends, FastAPI
from pydantic import BaseModel



class CreatePostIn(BaseModel):
    title:str
    content:str

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


app = FastAPI()

@app.get("/blogs/")
async def blogs_list(params : Annotated[dict, Depends(common_parameters)]):
    return {"results":{1,2,3,4,5}}

@app.get("/blog/{slug}")
async def root(slug:str, id:int):
    return {"message":"Hello World!"}

@app.post("/create")
async def create_post(reqBody:CreatePostIn = Body()):
    return reqBody



if __name__ == "__main__":
    uvicorn.run(app)