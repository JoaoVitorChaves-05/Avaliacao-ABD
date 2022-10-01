from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,create_engine, select

# <dbms>[+<driver>]://<user>:<pass>@<host>[:<port>][/<database>]
URL="mysql+mysqlconnector://root:root@127.0.0.1:3306/avaliacao_abd"
engine = create_engine(url=URL)

Base = declarative_base()

class Time(Base):
    __tablename__ = 'time_futebol'
    id = Column(Integer, primary_key=True)
    nome_time = Column(String(255), nullable=False)
    id_cidade = Column(Integer, ForeignKey('cidade.id'), nullable=False)
    id_estadio = Column(Integer, ForeignKey('estadio.id'), nullable=True)
    treinador = relationship('treinador')
    jogador = relationship('jogador')
    campeonato = relationship('campeonato')
    jogo = relationship('jogo')

class Treinador(Base):
    __tablename__ = 'treinador'
    id = Column(Integer, primary_key=True)
    nome_treinador = Column(String(255), nullable=False)
    id_time = Column(Integer, ForeignKey('time_futebol.id'), nullable=False)

class Jogador(Base):
    __tablename__ = 'jogador'
    id = Column(Integer, primary_key=True)
    nome_jogador = Column(String(255), nullable=False)
    id_time = Column(Integer, ForeignKey('time_futebol.id'), nullable=False)

class TimeCampeonato(Base):
    __tablename__ = 'time_campeonato'
    id = Column(Integer, primary_key=True)
    id_time = Column(Integer, ForeignKey('time_futebol.id'), nullable=False)
    id_campeonato = Column(Integer, ForeignKey('time_futebol.id'), nullable=False)
    pontos = Column(Integer, nullable=False)

class Campeonato(Base):
    __tablename__ = 'campeonato'
    id = Column(Integer, primary_key=True)
    nome_campeonato = Column(String(255), nullable=False)
    n_max_times = Column(Integer, nullable=False)
    time_campeonato = relationship('time_campeonato')

class Estadio(Base):
    __tablename__ = 'estadio'
    id = Column(Integer, primary_key=True)
    nome_estadio = Column(String(255), nullable=False)
    capacidade = Column(Integer, nullable=False)
    id_cidade = Column(Integer, ForeignKey('cidade.id'), nullable=False)
    time_futebol = relationship('time_futebol')
    jogo = relationship('jogo')

class Cidade(Base):
    __tablename__ = 'cidade'
    id = Column(Integer, primary_key=True)
    nome_cidade = Column(String(255), nullable=False)
    time_futebol = relationship('time_futebol')
    estadio = relationship('estadio')

class Jogo(Base):
    __tablename__ = 'jogo'
    id = Column(Integer, primary_key=True)
    id_time_visitante = Column(Integer, ForeignKey('time_futebol.id'), nullable=False)
    id_time_mandante = Column(Integer, ForeignKey('time_futebol.id'), nullable=False)
    data_jogo = Column(DateTime, nullable=True)
    id_estadio = Column(Integer, ForeignKey('estadio.id'), nullable=True)
    id_campeonato = Column(Integer, ForeignKey('campeonato.id'), nullable=True)

Base.metadata.create_all(engine)