# coding: utf-8


def limpar_arquivo(arquivo):
    with open(arquivo, "w") as f:
        f.write("")


def escrever_arquivo(de, para, retirar_header=False):
    with open(de, "r") as arquivo_de:
        contador = 0
        data = arquivo_de.readline()
        while data:
            with open(para, "a") as arquivo_para:
                if retirar_header and contador == 0:
                    contador += 1
                    data = arquivo_de.readline()
                    continue
                arquivo_para.write(data)
            data = arquivo_de.readline()


def main():
    # Solução do Professor
    para = "desafios/assets/dados_3.csv"
    limpar_arquivo(para)
    escrever_arquivo("desafios/assets/dados_1.csv", para)
    escrever_arquivo("desafios/assets/dados_2.csv", para, True)


if __name__ == "__main__":
    main()
