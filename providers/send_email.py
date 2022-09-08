from fastapi_mail import FastMail,ConnectionConfig,MessageSchema

from schemas.schemas import SendEmail

async def send_email(email:SendEmail, password):
    conf = ConnectionConfig(
    MAIL_USERNAME = "portifoli.paulo@gmail.com",
    MAIL_PASSWORD = "",
    MAIL_FROM = "portifoli.paulo@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
    html=f''' SENHA : {password}
'''
    message = MessageSchema(
        subject="Senha da conta",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        body=html,
        subtype="html"
        )
    fm=FastMail(conf)
    await fm.send_message(message)
