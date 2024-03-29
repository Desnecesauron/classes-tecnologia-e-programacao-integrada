# Validador de Números de Telefones

import re
import pytest


def validar_telefone(telefone):
    return bool(re.match(r"^\([1-9]{2}\) [0-9]{4,5}-[0-9]{4}$", telefone))


def test_validar_telefone():
    assert validar_telefone("(11) 1234-5678") == True
    assert validar_telefone("(11) 12345-6789") == True
    assert validar_telefone("(11) 1234-56789") == False
    assert validar_telefone("(11) 123-5678") == False
    assert validar_telefone("(11) 1234-567") == False
    assert validar_telefone("(11) 1234-5678 ") == False
    assert validar_telefone("11) 1234-5678") == False
    assert validar_telefone("(11 1234-5678") == False
