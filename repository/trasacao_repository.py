
from schemas.schemas import TransacoesInput,ImportacaoRealizadasInput
from models.transacoesModels import  Transacao, ImportacaoRealizadas

from database.connection import async_session
from sqlalchemy.future import select

class TransacaoRepository:
    async def save_transacao(self,transacao:TransacoesInput):
        async with async_session() as session:
            async with session.begin():
                transacao=Transacao(banco_origem=transacao.banco_origem,
                    agencia_origem=transacao.agencia_origem,
                    conta_origem=transacao.conta_origem,
                    banco_destino=transacao.banco_destino,
                    agencia_destino=transacao.agencia_destino,
                    conta_destino=transacao.conta_destino,
                    valor_transação=transacao.valor_transação,
                    data_transacao=transacao.data_hora
                    )
                session.add(transacao)
                await session.commit()
                return transacao
    async def date_transacao(self,dates:ImportacaoRealizadasInput):
        async with async_session() as session:
            async with session.begin():
                session.add(ImportacaoRealizadas(data_transacao=dates.data_transacao,data_importacao=dates.data_importacao,id_user=dates.id_user,id_transaçoes=dates.id_transaçoes)) 
                await session.commit()

    async def get_date_transacao(self):
        async with async_session() as session:
            result= await session.execute(select(ImportacaoRealizadas).order_by(ImportacaoRealizadas.data_importacao.desc()))
            return result.scalars().all()
#.order_by(ImportacaoRealizadas.data_importacao.desc())