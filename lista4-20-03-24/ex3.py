# Verificador de Senhas Seguras

import pytest


def senha_segura(senha):
    if len(senha) < 8:
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char in "!@#$%&*()_+-=[]{}|;:,.<>?/" for char in senha):
        return False
    return True


def test_senha_segura():
    assert senha_segura("senha") == False
    assert senha_segura("senha123") == False
    assert senha_segura("SENHA123") == False
    assert senha_segura("senha123!") == False
    assert senha_segura("SENHa123!") == True
    assert senha_segura("senhA123@") == True
    assert senha_segura("senhA123@#") == True
    assert senha_segura("senha123@#A") == True
    assert senha_segura("senha123@#Aa") == True
    assert senha_segura("senha123@#") == False
