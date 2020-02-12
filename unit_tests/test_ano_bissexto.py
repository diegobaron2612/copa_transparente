#!/usr/bin/env python3


def eh_ano_bissexto(ano):
    if ano % 4 != 0:
        return False

    if ano % 400 != 0 and ano % 100 == 0:
        return False

    return True


def test_ano_bissexto_2000():
    resposta = eh_ano_bissexto(2000)
    assert resposta is True


def test_ano_bissexto_2019():
    resposta = eh_ano_bissexto(2019)
    assert resposta is False


def test_ano_bissexto_2020():
    resposta = eh_ano_bissexto(2020)
    assert resposta is True


def test_ano_bissexto_1800():
    resposta = eh_ano_bissexto(1800)
    assert resposta is False
