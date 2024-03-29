# Ordenação de uma lista

import pytest


def ordenar_crescente(lista):
    return sorted(lista)


def ordenar_decrescente(lista):
    return sorted(lista, reverse=True)


def test_ordenar_crescente():
    assert ordenar_crescente([3, 2, 1]) == [1, 2, 3]
    assert ordenar_crescente([1, 2, 3]) == [1, 2, 3]
    assert ordenar_crescente([3, 1, 2]) == [1, 2, 3]
    assert ordenar_crescente([1, 3, 2]) == [1, 2, 3]


def test_ordenar_decrescente():
    assert ordenar_decrescente([3, 2, 1]) == [3, 2, 1]
    assert ordenar_decrescente([1, 2, 3]) == [3, 2, 1]
    assert ordenar_decrescente([3, 1, 2]) == [3, 2, 1]
    assert ordenar_decrescente([1, 3, 2]) == [3, 2, 1]
