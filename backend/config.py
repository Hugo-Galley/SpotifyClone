import json
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import colorlog
import os
from models import Base

def load_config():
    with open("variables.json") as f:
        return json.load(f)

def configBdd():
    user = data['Bdd']['User']
    password = data['Bdd']['Password']
    host = data['Bdd']['Host']
    port = data['Bdd']['Port']
    database = data['Bdd']['DataBase']

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=int(port)
    )
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`")
    connection.close()

    engine = create_engine(f"mysql+pymysql://{data['Bdd']['User']}:{data['Bdd']['Password']}@{data['Bdd']['Host']}:{data['Bdd']['Port']}/{data['Bdd']['DataBase']}")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    return db

data =load_config()
db = configBdd()

def setupLog():

    os.makedirs("log", exist_ok=True)
    loggger = logging.getLogger()
    loggger.setLevel(logging.DEBUG)

    console_handler = colorlog.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        )
    )

    file_handler = logging.FileHandler(data["Log"]["FileDestination"], mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.propagate = False

    uvicorn_acces_logger = logging.getLogger("uvicorn_acces")
    uvicorn_acces_logger.setLevel(logging.INFO)

    fastapi_logger = logging.getLogger("fastapi")
    fastapi_logger.setLevel(logging.INFO)

    loggger.addHandler(console_handler)
    loggger.addHandler(file_handler)
