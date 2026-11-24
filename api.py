
import os
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from modelos import Exercicio, ExercicioResposta, Usuario
from banco import (
    buscar_usuario_por_email,
    verificar_senha,
    salvar_usuario,
    gerar_hash_senha,
    salvar_exercicio,
    listar_exercicios,
    atualizar_exercicio,
    excluir_exercicio
)

app = FastAPI()

CHAVE_SECRETA = os.getenv("JWT_SECRET", "chave-temporaria-para-desenvolvimento")
ALGORITMO = "HS256"
TEMPO_TOKEN_MINUTOS = 30

seguranca = HTTPBearer()


def usuario_atual(
    credenciais: HTTPAuthorizationCredentials = Depends(seguranca)
):
    token = credenciais.credentials

    try:
        payload = jwt.decode(
            token,
            CHAVE_SECRETA,
            algorithms=[ALGORITMO]
        )

        usuario_id = payload.get("sub")

        if usuario_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        return {"id": int(usuario_id)}

    except (jwt.InvalidTokenError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado"
        )


@app.get("/")
def inicio():
    return {"mensagem": "AutoCuidado Gym API funcionando!"}


@app.get(
    "/exercicios",
    response_model=list[ExercicioResposta],
    dependencies=[Depends(usuario_atual)]
)
def listar_exercicios_api():
    return listar_exercicios()


@app.post(
    "/exercicios",
    dependencies=[Depends(usuario_atual)]
)
def criar_exercicio_api(exercicio: Exercicio):
    salvar_exercicio(
        exercicio.nome,
        exercicio.series,
        exercicio.repeticoes,
        exercicio.carga
    )
    return exercicio


@app.put(
    "/exercicios/{id}",
    dependencies=[Depends(usuario_atual)]
)
def atualizar_exercicio_api(id: int, exercicio: Exercicio):
    atualizar_exercicio(
        id,
        exercicio.nome,
        exercicio.series,
        exercicio.repeticoes,
        exercicio.carga
    )

    return {
        "mensagem": "Exercício atualizado com sucesso",
        "id": id,
        "exercicio": exercicio
    }


@app.delete(
    "/exercicios/{id}",
    dependencies=[Depends(usuario_atual)]
)
def excluir_exercicio_api(id: int):
    excluir_exercicio(id)

    return {
        "mensagem": "Exercício excluído com sucesso",
        "id": id
    }


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    senha_hash = gerar_hash_senha(usuario.senha)

    salvar_usuario(usuario.email, senha_hash)

    return {"mensagem": "Usuário criado com sucesso"}


@app.post("/login")
def login(usuario: Usuario):
    usuario_db = buscar_usuario_por_email(usuario.email)

    if usuario_db is None or not verificar_senha(
        usuario.senha,
        usuario_db["senha_hash"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou senha incorretos"
        )

    agora = datetime.now(timezone.utc)

    payload = {
        "sub": str(usuario_db["id"]),
        "exp": agora + timedelta(minutes=TEMPO_TOKEN_MINUTOS)
    }

    token = jwt.encode(
        payload,
        CHAVE_SECRETA,
        algorithm=ALGORITMO
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
