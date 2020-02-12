#!/usr/bin/env python3
import pytest

@pytest.fixture
def lista_1():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def quantidade_na_lista(lista):
    return len(lista)


def test_lista_um(lista_1):
    assert quantidade_na_lista(lista_1) == 9


def test_lista_um_de_novo(lista_1):
    assert quantidade_na_lista(lista_1) == 9
