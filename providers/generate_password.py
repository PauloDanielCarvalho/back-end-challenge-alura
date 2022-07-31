import string
from random import choice

async def generate_password():
    valores=''
    valores+=string.ascii_letters
    valores+=string.digits
    valores+=string.punctuation
    senha=''
    for i in range(6):
        senha+=choice(valores)
    return senha