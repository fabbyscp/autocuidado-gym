import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def conectar():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DATABASE"),
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )

def salvar_exercicio(nome, series, repeticoes, carga):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO exercicios (nome, series, repeticoes, carga)
        VALUES (%s, %s, %s, %s)
        """,
        (nome, series, repeticoes, carga)
    )


    conexao.commit()
    cursor.close()
    conexao.close()

def listar_exercicios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM exercicios")

    exercicios = cursor.fetchall()

    cursor.close()
    conexao.close()

    return exercicios