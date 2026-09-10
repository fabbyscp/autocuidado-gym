from pydantic import BaseModel


class Exercicio(BaseModel):
    nome: str
    series: int
    repeticoes: int
    carga: float