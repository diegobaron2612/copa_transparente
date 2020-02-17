import pytest

from ..desafios import duplicados


@pytest.fixture
def dados1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def dados2():
    return [6, 7, 8, 9, 10]


@pytest.fixture
def dados3():
    return [3, 4, 5, 6, 7]


@pytest.fixture
def dados4():
    return [1, 3, 8, 9]


def test_duplicados_sem_duplicados(dados1, dados2):
    resultado = duplicados(dados1, dados2)
    assert resultado == []


def test_duplicados_um(dados1, dados3):
    resultado = duplicados(dados1, dados3)
    assert resultado == [3, 4, 5]


def test_duplicados_dois(dados2, dados4):
    resultado = duplicados(dados2, dados4)
    assert resultado == [8, 9]


# class Teste(unittest.TestCase):
#     def setUp(self):
#         self.dados1 = []
#         self.dados2 = []
#         self.dados3 = []
#         self.dados4 = []
