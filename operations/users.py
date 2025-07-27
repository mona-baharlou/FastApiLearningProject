import sqlalchemy as sa
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User


class UserOperation:

    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, username: str, password: str) -> User:
        try:
            user = User(username=username, password=password)
            self.db_session.add(user)
            await self.db_session.commit()
            return user
        except Exception as e:
            await self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error during user creation: {str(e)}"
            )

    async def get_user_by_username(self, username: str) -> User:
        query = sa.select(User).where(User.username == username)

        async with self.db_session as session:
            data = await session.scalar(query)

            if data is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found !"
                    )
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
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found !"
                    )

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


