# coding: utf-8

from decimal import Decimal

total = Decimal("0")


def dec(element, index):
    try:
        return Decimal(element[index])
    except:
        return Decimal("0")


class QueryFile:
    def __init__(self, filename, operator=";"):
        self._file = open(filename, "r")
        self._operator = operator

    def __iter__(self):
        return self

    def __next__(self):
        data = self._file.readline()
        if not data:
            self._file.close()
            raise StopIteration
        return data.split(self._operator)


query = QueryFile("data/data/ExecucaoFinanceira.csv")
valores_totais = (dec(element, 5) for element in query)
total = sum(valores_totais)

print("Total gasto: {}".format(total))
