import pytest
from exercicios import criar_exercicio


def test_criar_exercicio():
    exercicio = criar_exercicio("Bíceps", 3, 10, 10)

    assert exercicio["nome"] == "Bíceps"
    assert exercicio["series"] == 3
    assert exercicio["repeticoes"] == 10
    assert exercicio["carga"] == 10


def test_exercicio_nao_pode_ter_zero_series():
    with pytest.raises(ValueError):
        criar_exercicio("Bíceps", 0, 10, 10)