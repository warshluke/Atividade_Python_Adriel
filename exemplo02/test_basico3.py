def somar(a,b):
    return a+b


def comprimento(lista):
    return len(lista)
def teste_somar():
    assert somar(2,4) == 6
    assert somar(1,1) == 2

def teste_comprimento():
    assert comprimento([1,2,3,4,1,5,1]) == 7
    assert comprimento('Washington') == 10

def email_valido(email):
    return '@' in email and '.' in email

def test_email_valido():
    assert email_valido('ADD@gmail.com') == True
    assert email_valido("mayconX@Outlook.com.br") ==  True

def dividir(a,b):
    if b== 0:
        return None
    return a / b

def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(1,0) == None
    