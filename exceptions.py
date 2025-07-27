from fastapi import HTTPException, status


class UserNotFound(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User not found!"
    pass



