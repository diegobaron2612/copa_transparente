x = input('Digite o primeiro número: ')
y = input('Digite o segundo número: ')


class Calculadora:

    @staticmethod
    def dividir(x, y):
        resultado = int(x) / int(y)
        print(resultado)
        return resultado


try:
    resultado = Calculadora.dividir(x, y)
except ZeroDivisionError as ex:
    print('Divisão por zero')
    raise ex
except ValueError as ex:
    print('Valor inválido')
    raise ex
except TypeError as ex:
    print('Tipo inválido')
    raise ex
