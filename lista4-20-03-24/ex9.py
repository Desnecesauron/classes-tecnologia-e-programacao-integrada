# Implemente um sistema simples de reservas de passagens aéreas

from datetime import datetime
from typing import List, Dict
import pytest


class Voo:
    def __init__(self, origem: str, destino: str, data: str, horario: str, preco: float):
        self.origem = origem
        self.destino = destino
        self.data = datetime.strptime(data, "%d/%m/%Y")
        self.horario = horario
        self.preco = preco

    def __eq__(self, other):
        if isinstance(other, Voo):
            return self.origem == other.origem and self.destino == other.destino and self.data == other.data and self.horario == other.horario and self.preco == other.preco
        return False

    def __repr__(self):
        return f"Voo({self.origem}, {self.destino}, {self.data.strftime('%d/%m/%Y')}, {self.horario}, {self.preco})"


class Reserva:
    def __init__(self, voo: Voo, quantidade: int):
        self.voo = voo
        self.quantidade = quantidade

    def __eq__(self, other):
        if isinstance(other, Reserva):
            return self.voo == other.voo and self.quantidade == other.quantidade
        return False

    def __repr__(self):
        return f"Reserva({self.voo}, {self.quantidade})"


class SistemaReservas:
    def __init__(self):
        self.voos: List[Voo] = []
        self.reservas: List[Reserva] = []

    def adicionar_voo(self, voo: Voo):
        self.voos.append(voo)

    def pesquisar_voos(self, origem: str, destino: str, data: str):
        return [voo for voo in self.voos if voo.origem == origem and voo.destino == destino and voo.data.strftime("%d/%m/%Y") == data]

    def realizar_reserva(self, voo: Voo, quantidade: int):
        if quantidade > 0:
            self.reservas.append(Reserva(voo, quantidade))

    def visualizar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, reserva: Reserva):
        self.reservas.remove(reserva)

def test_sistema_reservas():
    sistema = SistemaReservas()
    voo1 = Voo("GRU", "GIG", "01/01/2020", "08:00", 1000.0)
    voo2 = Voo("GIG", "GRU", "01/01/2020", "10:00", 1000.0)
    sistema.adicionar_voo(voo1)
    sistema.adicionar_voo(voo2)
    assert sistema.pesquisar_voos("GRU", "GIG", "01/01/2020") == [voo1]
    assert sistema.pesquisar_voos("GIG", "GRU", "01/01/2020") == [voo2]
    sistema.realizar_reserva(voo1, 1)
    assert sistema.visualizar_reservas() == [Reserva(voo1, 1)]
    sistema.cancelar_reserva(Reserva(voo1, 1))
    assert sistema.visualizar_reservas() == []
    sistema.realizar_reserva(voo1, 0)
    assert sistema.visualizar_reservas() == []
    sistema.realizar_reserva(voo1, -1)
    assert sistema.visualizar_reservas() == []
    sistema.realizar_reserva(voo1, 1)
    sistema.realizar_reserva(voo1, 1)
    assert sistema.visualizar_reservas() == [Reserva(voo1, 1), Reserva(voo1, 1)]
