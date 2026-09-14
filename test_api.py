from fastapi.testclient import TestClient
from api import app
from banco import listar_exercicios


client = TestClient(app)


def test_listar_exercicios():
    client.post(
        "/exercicios",
        json={
            "nome": "Supino",
            "series": 3,
            "repeticoes": 10,
            "carga": 20
        }
    )

    client.post(
        "/exercicios",
        json={
            "nome": "Leg Press",
            "series": 3,
            "repeticoes": 12,
            "carga": 50
        }
    )

    resposta = client.get("/exercicios")

    assert resposta.status_code == 200
    assert len(resposta.json()) == 2
    assert resposta.json()[0][1] == "Supino"
    assert resposta.json()[1][1] == "Leg Press"

def test_criar_exercicio():
    resposta = client.post(
        "/exercicios",
        json={
            "nome": "Agachamento",
            "series": 3,
            "repeticoes": 12,
            "carga": 20
        }
    )

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Agachamento"

    exercicios = listar_exercicios()

    assert len(exercicios) == 1
    assert exercicios[0][1] == "Agachamento"

def test_criar_exercicio_sem_nome():
    resposta = client.post(
        "/exercicios",
        json={
            "nome": "",
            "series": 3,
            "repeticoes": 12,
            "carga": 20
        }
    )

    assert resposta.status_code == 422