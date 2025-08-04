from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    password: str


class UpdateProfileInput(BaseModel):
    old_username: str
    new_username: str


class DeleteAccountInput(BaseModel):
    username: str
    password: str
