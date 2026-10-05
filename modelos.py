from pydantic import BaseModel, Field

class Exercicio(BaseModel):
    nome: str = Field(min_length=1)
    series: int
    repeticoes: int
    carga: float


class ExercicioResposta(BaseModel):
    id: int
    nome: str
    series: int
    repeticoes: int
    carga: float