import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash_senha(senha):
    return pwd_context.hash(senha)


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

    exercicios = [
        {
            "id": linha[0],
            "nome": linha[1],
            "series": linha[2],
            "repeticoes": linha[3],
            "carga": linha[4]
        }
        for linha in cursor.fetchall()
    ]

    cursor.close()
    conexao.close()

    return exercicios


def atualizar_exercicio(id, nome, series, repeticoes, carga):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE exercicios
        SET nome = %s,
            series = %s,
            repeticoes = %s,
            carga = %s
        WHERE id = %s
        """,
        (nome, series, repeticoes, carga, id)
    )

    conexao.commit()
    cursor.close()
    conexao.close()


def excluir_exercicio(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM exercicios WHERE id = %s",
        (id,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

def salvar_usuario(email, senha_hash):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO usuarios (email, senha_hash)
        VALUES (%s, %s)
        """,
        (email, senha_hash)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

def buscar_usuario_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, email, senha_hash FROM usuarios WHERE email = %s",
        (email,)
    )

    linha = cursor.fetchone()
    cursor.close()
    conexao.close()

    if linha is None:
        return None

    return {
        "id": linha[0],
        "email": linha[1],
        "senha_hash": linha[2]
    }


def verificar_senha(senha, senha_hash):
    return pwd_context.verify(senha, senha_hash)