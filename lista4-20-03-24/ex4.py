# Validador de E-mails

import pytest


def email_valido(email):
    if not "@" in email:
        return False
    if email.count("@") != 1:
        return False
    if not "." in email:
        return False
    if email.count(".") > 1:
        return False
    if email[-1] == ".":
        return False
    if len(email) < 6:
        return False
    if len(email) > 320:
        return False
    return True


def test_email_valido():
    assert email_valido("email") == False
    assert email_valido("email@") == False
    assert email_valido("email.com") == False
    assert email_valido("email@com") == False
    assert email_valido("email@com.") == False
    assert email_valido("email@gmail.com") == True
