from exercicios import criar_exercicio
from treinos import criar_treino

if __name__ == "__main__":
    exercicios = []

    continuar = "s"

    while continuar == "s":
        nome = input("Nome do exercício: ")
        series = int(input("Séries: "))
        repeticoes = int(input("Repetições: "))
        carga = float(input("Carga (kg): "))

        exercicio = criar_exercicio(nome, series, repeticoes, carga)
        exercicios.append(exercicio)

        continuar = input("Adicionar outro exercício? (s/n): ")

    data = input("Data do treino: ")

    treino = criar_treino(data, exercicios)

    print(treino)