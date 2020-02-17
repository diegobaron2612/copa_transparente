def duplicados(lista_1, lista_2):
    return list(set(lista_1) & set(lista_2))


def main():
    try:
        happynumbers = open("assets/happynumbers.txt", "r")
        primenumbers = open("assets/primenumbers.txt", "r")
        lista_1 = happynumbers.read().split("\n")
        lista_2 = primenumbers.read().split("\n")
        happynumbers.close()
        primenumbers.close()
        return duplicados(lista_1, lista_2)
    except Exception as ex:
        print("Ocorreu algo errado...")
        raise ex


if __name__ == "__main__":
    resultado = main()
    print(sorted(resultado, key=lambda x: int(x)))
