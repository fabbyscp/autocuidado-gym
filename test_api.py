
from datetime import datetime, timedelta, timezone

import jwt
from fastapi.testclient import TestClient

from api import app, CHAVE_SECRETA, ALGORITMO
from banco import listar_exercicios

client = TestClient(app)


def obter_headers():
    token = jwt.encode(
        {
            "sub": "1",
            "exp": datetime.now(timezone.utc) + timedelta(minutes=5)
        },
        CHAVE_SECRETA,
        algorithm=ALGORITMO
    )

    return {"Authorization": f"Bearer {token}"}


def test_listar_exercicios():
    headers = obter_headers()

    client.post(
        "/exercicios",
        json={
            "nome": "Supino",
            "series": 3,
            "repeticoes": 10,
            "carga": 20
        },
        headers=headers
    )

    client.post(
        "/exercicios",
        json={
            "nome": "Leg Press",
            "series": 3,
            "repeticoes": 12,
            "carga": 50
        },
        headers=headers
    )

    resposta = client.get("/exercicios", headers=headers)

    assert resposta.status_code == 200


def test_criar_exercicio():
    headers = obter_headers()

    resposta = client.post(
        "/exercicios",
        json={
            "nome": "Agachamento",
            "series": 3,
            "repeticoes": 12,
            "carga": 20
        },
        headers=headers
    )

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Agachamento"


def test_criar_exercicio_sem_nome():
    resposta = client.post(
        "/exercicios",
        json={
            "nome": "",
            "series": 3,
            "repeticoes": 12,
            "carga": 20
        },
        headers=obter_headers()
    )

    assert resposta.status_code == 422
