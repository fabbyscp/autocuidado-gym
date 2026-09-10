import sqlite3
DATABASE = "autocuidado.db"

def criar_tabela():
    conexao = sqlite3.connect(DATABASE)
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            series INTEGER NOT NULL,
            repeticoes INTEGER NOT NULL,
            carga REAL NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_exercicio(nome, series, repeticoes, carga):
    conexao = sqlite3.connect(DATABASE)
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO exercicios (nome, series, repeticoes, carga)
        VALUES (?, ?, ?, ?)
    """, (nome, series, repeticoes, carga))

    conexao.commit()
    conexao.close()

def listar_exercicios():
    conexao = sqlite3.connect(DATABASE)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM exercicios")

    exercicios = cursor.fetchall()

    conexao.close()

    return exercicios