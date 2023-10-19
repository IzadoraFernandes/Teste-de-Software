import pytest
from identifail import Identifail

def test_validar_entrada_caso_valido():
    identificacao = Identifail("ID", "A12345")
    resultado = identificacao.validar_entrada()
    assert resultado == "Válido"

def test_validar_entrada_caso_invalido_letra_inicial():
    identificacao = Identifail("ID", "12345A")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"

def test_validar_entrada_caso_invalido_comprimento():
    identificacao = Identifail("ID", "AB123456")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"

def test_validar_entrada_caso_invalido_em_branco():
    identificacao = Identifail("ID", "")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"

def test_validar_entrada_caso_invalido_caracter_especial():
    identificacao = Identifail("ID", "A@1234")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"
