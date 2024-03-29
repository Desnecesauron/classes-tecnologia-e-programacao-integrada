# Diferença entre datas

import pytest


from datetime import datetime


def diferenca_datas(data1, data2, unidade):
    data1 = datetime.strptime(data1, "%d/%m/%Y")
    data2 = datetime.strptime(data2, "%d/%m/%Y")
    diferenca = data2 - data1
    if unidade == "dias":
        return diferenca.days
    if unidade == "meses":
        return diferenca.days // 30
    if unidade == "anos":
        return diferenca.days // 365
    if unidade == "horas":
        return diferenca.days * 24
    if unidade == "minutos":
        return diferenca.days * 24 * 60


def test_diferenca_datas():
    assert diferenca_datas("01/01/2020", "01/01/2020", "dias") == 0
    assert diferenca_datas("01/01/2020", "02/01/2020", "dias") == 1
    assert diferenca_datas("01/01/2020", "01/02/2020", "dias") == 31
    assert diferenca_datas("01/01/2020", "01/01/2021", "dias") == 366
    assert diferenca_datas("01/01/2021", "01/01/2022", "dias") == 365
    assert diferenca_datas("01/01/2020", "01/01/2020", "meses") == 0
    assert diferenca_datas("01/01/2020", "02/01/2020", "meses") == 0
    assert diferenca_datas("01/01/2020", "01/02/2020", "meses") == 1
    assert diferenca_datas("01/01/2020", "01/01/2021", "meses") == 12
    assert diferenca_datas("01/01/2020", "01/01/2020", "anos") == 0
    assert diferenca_datas("01/01/2020", "02/01/2020", "anos") == 0
    assert diferenca_datas("01/01/2020", "01/02/2020", "anos") == 0
    assert diferenca_datas("01/01/2020", "01/01/2021", "anos") == 1
    assert diferenca_datas("01/01/2020", "01/01/2020", "horas") == 0
    assert diferenca_datas("01/01/2020", "02/01/2020", "horas") == 24
    assert diferenca_datas("01/01/2020", "01/02/2020", "horas") == 744
    assert diferenca_datas("01/01/2020", "01/01/2021", "horas") == 8784
    assert diferenca_datas("01/01/2021", "01/01/2022", "horas") == 8760
    assert diferenca_datas("01/01/2020", "01/01/2020", "minutos") == 0
