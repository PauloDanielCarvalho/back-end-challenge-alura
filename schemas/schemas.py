
from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime




class TransacoesInput(BaseModel):
    banco_origem:str
    agencia_origem:int
    conta_origem:str
    banco_destino:str
    agencia_destino:int
    conta_destino:str
    valor_transação:float
    data_hora:datetime
    

class ImportacaoRealizadasInput(BaseModel):
    data_transacao:datetime
    data_importacao:datetime
    id_user:int
    id_transaçoes:int
    

class UserInput(BaseModel):
    name:str
    email:EmailStr

class SendEmail(BaseModel):
    email:List[EmailStr]
    class Config:
        orm_mode = True

class LoginData(BaseModel):
    email:EmailStr
    password:str

class LoginResponse(BaseModel):
    email:EmailStr
    password:str
    class Config:
        orm_mode = True