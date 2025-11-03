from test_basico3 import *


def teste_email_valido():
    assert email_valido("ADRIEL@GMAIL.COM") is True

def test_dividir():
    assert dividir(2,2) == 1