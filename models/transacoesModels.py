

from sqlalchemy import Column, Integer, String,Float,DateTime,ForeignKey
from database.connection import Base
from sqlalchemy.orm import relationship

class ImportacaoRealizadas(Base):
    __tablename__="ImportacaoRealizada"

    id=Column(Integer,primary_key=True, autoincrement=True)
    data_transacao=Column(DateTime)
    data_importacao=Column(DateTime)
    id_user=Column(Integer,ForeignKey('users.id'))
    id_transaçoes=Column(Integer,ForeignKey('transaçoes.id'))


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String)
    email=Column(String,unique=True,index=True)
    password=Column(String)
    transaçoes=relationship('Transacao',secondary="ImportacaoRealizada",back_populates="users",lazy='subquery')


class Transacao(Base):
    __tablename__="transaçoes"
    id=Column(Integer, primary_key=True, autoincrement=True)
    banco_origem=Column(String)
    agencia_origem=Column(Integer)
    conta_origem=Column(String)
    banco_destino=Column(String)
    agencia_destino=Column(Integer)
    conta_destino=Column(String)
    valor_transação=Column(Float)
    data_transacao=Column(DateTime)
    users=relationship('User',secondary="ImportacaoRealizada",back_populates="transaçoes")