from fastapi import HTTPException, status


class UserNotFound(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User not found!"
    pass


class UserExist(HTTPException):
    def __init__(self) -> None:
        self.status_code = 400
        self.detail = "Username exists!"
    pass
