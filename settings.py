import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PWD = os.environ.get("DATABASE_PWD")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PWD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
FILES_FOLDER = "./files/"