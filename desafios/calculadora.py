# calculadora.py


def dividir(x, y):
    try:
        resultado = int(x) / int(y)
        return resultado
    except ZeroDivisionError as ex:
        print('Divisão por zero')
        raise ex
    except ValueError as ex:
        print('Valor inválido')
        raise ex
    except TypeError as ex:
        print('Tipo inválido')
        raise ex


if __name__ == '__main__':
    operador = 'x'
    print('Bem vindo à calculadora!!!')
    while operador != '0':
        print('Por favor, digite a operação desejada(EX: +, -, *, /)\nOu "0" para sair: ', end='')
        operacao = input()

        if operacao == '/':
            x = input('Digite o primeiro valor: ')
            y = input('Digite o segundo valor: ')
            resultado = dividir(x, y)

        if operacao != '0':
            print('O resultado foi de:', resultado)
