from sqlalchemy import Column, Numeric, String

from database import Base


class TestSeplan(Base):
    __tablename__ = "test-seplan"
    __table_args__ = {"schema": "public"}
    id = Column(Numeric, primary_key=True, autoincrement=True)
    classificacao_atividade = Column(String(150), nullable=True)
    ano = Column(String(15), nullable=True)
    sigla_estado = Column(String(2), nullable=True)
    variavel = Column(String(150),nullable=True)
    quantidade = Column(String(15), nullable=True)
