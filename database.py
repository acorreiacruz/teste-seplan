from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, declarative_base, sessionmaker
from typing import List
from settings import DATABASE_URL
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - DATABASE - %(levelname)s - %(message)s"
)

engine = create_engine(url=DATABASE_URL)
DBSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base: DeclarativeBase = declarative_base()


def create_tables():
    try:
        logging.info("Criando as tabelas no banco ...")
        Base.metadata.create_all(engine)
        logging.info("Tabelas criadas com sucesso !")
    except Exception as error:
        logging.error(f"Erro ao tentar criar as tabelas no banco: {str(error)}")


def drop_tables():
    try:
        logging.info("Excluindo as tabelas do banco ...")
        Base.metadata.drop_all(engine)
        logging.info("Tabelas excluidas com sucesso !")
    except Exception as error:
        logging.error(f"Erro ao tentar excluir as tabelas do banco: {str(error)}")


def add_records(instances:List[DeclarativeBase], session: Session) -> None:
    try:
        logging.info("Adicionando dados no banco ...")
        session.add_all(instances)
        session.commit()
        logging.info("Dados adicionados com sucesso !")
    except Exception as error:
        logging.error(f"Erro ao adicionar dados no banco: {str(error)}")
        session.rollback()
    finally:
        session.close()
