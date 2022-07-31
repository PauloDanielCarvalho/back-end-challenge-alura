
from fastapi import APIRouter,HTTPException,status
from providers.send_email import send_email

from providers.generate_password import generate_password
from providers.hash_provider import get_password_hash,verify_password
from schemas.schemas import LoginData, LoginResponse, SendEmail, UserInput
from repository.user_repository import UserRepository

user_router=APIRouter()


@user_router.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup(user:UserInput):
    password_hash = await generate_password()
    
    await UserRepository.create_user(user,await get_password_hash(password_hash))
    await send_email(SendEmail(email=[user.email]),password_hash)
    
async def login(login_data:LoginData): 
    user= await UserRepository.get_email(login_data.email)
    
    print(await login_data.password,user.password)
        