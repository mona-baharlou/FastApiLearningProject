import sqlalchemy as sa
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
            print("Error during user creation:", e)
            await self.db_session.rollback()
            raise

    async def get_user_by_username(self, username: str) -> User:
        query = sa.select(User).where(User.username == username)

        async with self.db_session as session:
            data = await session.scalar(query)

            if data is None:
                raise  # ValidationErr("User not found! ")
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
                raise  # ValidationErr("User not found! ")

            await session.execute(update_query)
            await session.commit()

            data.username = new_username

            return data



