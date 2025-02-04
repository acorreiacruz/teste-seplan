import logging
import os
from typing import List

import pandas as pd

from database import DBSession, add_records
from models import TestSeplan
from settings import FILES_FOLDER
from state_acronyms import state_acronyms

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - PROCESS - %(levelname)s - %(message)s"
)


class Process:

    def __init__(self):
        self.__db_session = DBSession()

    def main(self) -> None:
        try:
            files = os.listdir(FILES_FOLDER)
            logging.info(f"Total de arquivos a serem processados: {len(files)}")
            for file in files:
                try:
                    logging.info(f"Processando o arquivo: {file}")
                    records: List[dict] = []
                    file_path = f"{FILES_FOLDER}{file}"
                    excel_file = pd.ExcelFile(file_path)
                    sheet_names = excel_file.sheet_names[:-1]
                    df = pd.concat(
                        [
                            pd.read_excel(excel_file, sheet_name=sheet)
                            for sheet in sheet_names
                        ]
                    )
                    df.ffill(axis=1, inplace=True)
                    year_column = 2
                    year_line = 2
                    cnae_line = 3
                    variable = df.iloc[0, 0]
                    total_columns = len(df.columns)
                    for row, state in enumerate(df.iloc[:, 0]):
                        if state not in state_acronyms:
                            continue
                        for column in range(year_column, total_columns):
                            records.append(
                                {
                                    "classificacao_atividade": df.iat[
                                        cnae_line, column
                                    ].strip(),
                                    "ano": str(df.iat[year_line, column]).strip(),
                                    "sigla_estado": state_acronyms.get(state),
                                    "variavel": variable.strip(),
                                    "quantidade": str(df.iat[row, column]).strip(),
                                }
                            )
                    logging.info(
                        f"Numero de registros para o arquivo {file}: {len(records)}"
                    )
                    records = [TestSeplan(**record) for record in records]
                    add_records(records, self.__db_session)
                except Exception as error:
                    logging.error(f"Erro ao processar o arquivo {file}: {str(error)}")
        except Exception as error:
            logging.error(f"Erro ao iniciar o script: {str(error)}")
        finally:
            self.__db_session.close()


def run():
    Process().main()
