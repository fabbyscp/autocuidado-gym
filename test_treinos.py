from treinos import criar_treino


def test_criar_treino():
    exercicios = [
        {
            "nome": "Bíceps",
            "series": 3,
            "repeticoes": 10,
            "carga": 10
        }
    ]

    treino = criar_treino("04/09/2026", exercicios)

    assert treino["data"] == "04/09/2026"
    assert treino["exercicios"] == exercicios