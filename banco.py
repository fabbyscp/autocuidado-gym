import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def conectar():
    return psycopg2.connect(
        host="localhost",
        database="autocuidado_gym",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )