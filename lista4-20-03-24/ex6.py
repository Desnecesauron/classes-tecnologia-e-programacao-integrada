# Contador de palavras em um texto

import pytest


def contar_palavras(texto):
    return len(texto.split())


def test_contar_palavras():
    assert contar_palavras("um dois tres") == 3
    assert contar_palavras("um dois tres quatro") == 4
    assert contar_palavras("um dois tres quatro cinco") == 5
    assert contar_palavras("um dois tres quatro cinco seis") == 6
