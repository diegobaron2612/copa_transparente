# test_aniversarios.py
import pytest
from desafios import retornar_aniversario


@pytest.fixture
def aniversarios():
    return {
        'vinicius': '24/09/1993',
        'diego': '26/12/1985',
        'leandro': '04/08/1978',
        'edina': '09/06/1983',
        'carol': '22/04/1981',
        'jose': '16/07/1978',
    }


def test_aniversario_inexistente(aniversarios):
    pessoa = 'einstein'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado is None


def test_aniversario_vinicius(aniversarios):
    pessoa = 'vinicius'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado == '24/09/1993'


def test_aniversario_diego(aniversarios):
    pessoa = 'diego'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado == '26/12/1985'


def test_aniversario_leandro(aniversarios):
    pessoa = 'leandro'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado == '04/08/1978'


def test_aniversario_edina(aniversarios):
    pessoa = 'edina'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado == '09/06/1983'


def test_aniversario_carol(aniversarios):
    pessoa = 'carol'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado == '22/04/1981'


def test_aniversario_jose(aniversarios):
    pessoa = 'jose'
    resultado = retornar_aniversario(pessoa, aniversarios)
    assert resultado == '16/07/1978'
