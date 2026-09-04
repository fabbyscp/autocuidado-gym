def criar_exercicio(nome, series, repeticoes, carga):
    if series <= 0:
        raise ValueError("Séries devem ser maiores que zero")

    return {
        "nome": nome,
        "series": series,
        "repeticoes": repeticoes,
        "carga": carga
    }