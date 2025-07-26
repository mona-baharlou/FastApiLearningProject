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
            print("❌ Error during user creation:", e)
            await self.db_session.rollback()
            raise
        