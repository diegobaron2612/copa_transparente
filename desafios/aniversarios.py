# aniversarios.py


def retornar_aniversario(pessoa, aniversarios):
    resultado = aniversarios.get(pessoa)
    return resultado


def printar_pessoas(aniversarios):
    for pessoa in aniversarios:
        print(pessoa.title())


def obter_datas_aniversario():
    aniversarios = {}
    with open('aniversarios.txt') as arquivo:
        for linha in arquivo:
            nome, aniversario = linha.split()
            aniversarios[nome] = aniversario
    return aniversarios


def main():
    print('-' * 10, 'Bem Vindo ao Dicionario de aniversarios',
          '-' * 10)
    print('Temos registrado os aniversários dessas pessoas:')
    aniversarios = obter_datas_aniversario()
    printar_pessoas(aniversarios)
    pessoa = input('Qual aniversário você quer olhar? ').lower()
    resultado = retornar_aniversario(pessoa, aniversarios)
    if resultado:
        print(f"{pessoa.title()} nasceu no dia {resultado}")
    else:
        print('Essa pessoa não existe em nosso dicionário')


if __name__ == '__main__':
    main()
