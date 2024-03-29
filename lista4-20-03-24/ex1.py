# Calculadora Simples

import pytest


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def test_soma():
    assert soma(1, 1) == 2
    assert soma(1, 2) == 3
    assert soma(2, 2) == 4
    assert soma(2, 3) == 5


def test_subtracao():
    assert subtracao(1, 1) == 0
    assert subtracao(1, 2) == -1
    assert subtracao(2, 2) == 0
    assert subtracao(2, 3) == -1


def test_multiplicacao():
    assert multiplicacao(1, 1) == 1
    assert multiplicacao(1, 2) == 2
    assert multiplicacao(2, 2) == 4
    assert multiplicacao(2, 3) == 6


def test_divisao():
    assert divisao(1, 1) == 1
    assert divisao(1, 2) == 0.5
    assert divisao(2, 2) == 1
    assert divisao(2, 3) == 2/3
