# Conversor de Moedas

import pytest


def dolar_para_euro(dolar):
    return dolar * 0.92


def euro_para_dolar(euro):
    return euro / 0.92


def real_para_dolar(real):
    return real / 5.3


def dolar_para_real(dolar):
    return dolar * 5.3


def test_dolar_para_euro():
    assert dolar_para_euro(1) == 0.92
    assert dolar_para_euro(2) == 1.84
    assert dolar_para_euro(3) == 2.7600000000000002
    assert dolar_para_euro(4) == 3.68


def test_euro_para_dolar():
    assert euro_para_dolar(1) == 1.0869565217391304
    assert euro_para_dolar(2) == 2.1739130434782608
    assert euro_para_dolar(3) == 3.260869565217391
    assert euro_para_dolar(4) == 4.3478260869565215


def test_real_para_dolar():
    assert real_para_dolar(1) == 0.18867924528301888
    assert real_para_dolar(2) == 0.37735849056603776
    assert real_para_dolar(3) == 0.5660377358490566
    assert real_para_dolar(4) == 0.7547169811320755


def test_dolar_para_real():
    assert dolar_para_real(1) == 5.3
    assert dolar_para_real(2) == 10.6
    assert dolar_para_real(3) == 15.899999999999999
    assert dolar_para_real(4) == 21.2
