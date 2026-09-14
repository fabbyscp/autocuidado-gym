import pytest
import banco


@pytest.fixture(autouse=True)
def banco_de_teste(monkeypatch):
    monkeypatch.setenv("POSTGRES_DATABASE", "autocuidado_gym_test")

    conexao = banco.conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM exercicios")

    conexao.commit()

    cursor.close()
    conexao.close()