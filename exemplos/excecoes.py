# JetBrains Mono
import sys


def dividir(x, y):
    try:
        resultado = int(x) / int(y)
        print(resultado)
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


operador = 'x'
print('Bem vindo à calculadora!!!')
while operador != '0':
    print('Para começar, digite a operação desejada: ')
    x = input()
