
from sqlalchemy.future import select
from database.connection import async_session

from schemas.schemas import UserInput
from models.transacoesModels import User

class UserRepository:
    async def create_user(user:UserInput,password_hash):
        async with async_session() as session:
            async with session.begin():
                session.add(User(name=user.name,email=user.email,password=password_hash))
                await session.commit()
    
    async def get_email(email):
        async with async_session() as session:
            user= await session.execute(select(User).where(User.email==email))
            return user.scalars().first()