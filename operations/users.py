import sqlalchemy as sa
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from exceptions import UserExist, UserNotFound
from schema.output import RegisterOutput
from utils.secrets import password_manager


class UserOperation:

    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, username: str, password: str) -> RegisterOutput:
        try:
            user_password = password_manager.hash(password)
            user = User(username=username, password=user_password)
            self.db_session.add(user)
            await self.db_session.commit()
            return RegisterOutput(username=user.username, id=user.id)
        except IntegrityError:
            await self.db_session.rollback()
            raise UserExist
        # except Exception as e:
            # await self.db_session.rollback()
            # raise HTTPException(
            #    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            #    detail=f"Error during user creation: {str(e)}"
            # )

    async def get_user_by_username(self, username: str) -> User:
        query = sa.select(User).where(User.username == username)

        async with self.db_session as session:
            data = await session.scalar(query)

            if data is None:
                raise UserNotFound
            return data

    async def update_username(self, old_username: str, new_username: str) -> User:
        query = sa.select(User).where(User.username == old_username)
        update_query = (
            sa.update(User)
            .where(User.username == old_username)
            .values(username=new_username)
        )

        async with self.db_session as session:
            data = await session.scalar(query)

            if data is None:
                raise UserNotFound

            await session.execute(update_query)
            await session.commit()

            data.username = new_username

            return data

    async def user_delete_account(self, username: str, password: str) -> None:

        delete_query = sa.delete(User).where(
            User.username == username,
            password == password
        )

        async with self.db_session as session:
            await session.execute(delete_query)
            await session.commit()


