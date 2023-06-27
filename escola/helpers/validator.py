import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    sliced_name = nome.split()
    for word in sliced_name:
        for char in word:
            if (not char.isalpha()) and ( not char == ' '):
                return False
    
    return True

def rg_valido(numero_do_rg):

    for char in numero_do_rg:
        if char.isalpha():
            return False

    return True

def celular_valido(numero_celular):
    """Verifica se o  celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta