def main():
    # Solução dos alunos
    dados1 = open("desafios/assets/dados_1.csv", "r")
    dados2 = open("desafios/assets/dados_2.csv", "r")

    lista1 = dados1.readlines()
    lista2 = dados2.readlines()[1:]
    lista3 = lista1 + lista2
    dados3 = open("desafios/assets/dados_3.csv", "w")
    dados3.writelines(lista3)
    dados1.close()
    dados2.close()
    dados3.close()
    return lista3


if __name__ == "__main__":
    main()
