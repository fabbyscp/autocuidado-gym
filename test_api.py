from fastapi.testclient import TestClient
from api import app


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