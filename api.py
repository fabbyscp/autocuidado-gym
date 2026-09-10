from fastapi import FastAPI
from exercicios import criar_exercicio
from modelos import Exercicio
from banco import salvar_exercicio
from banco import listar_exercicios

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "AutoCuidado Gym API funcionando!"}


@app.get("/exercicios")
def listar_exercicios_api():
    return listar_exercicios()

@app.post("/exercicios")
def criar_exercicio_api(exercicio: Exercicio):
    salvar_exercicio(
        exercicio.nome,
        exercicio.series,
        exercicio.repeticoes,
        exercicio.carga
    )

    return exercicio