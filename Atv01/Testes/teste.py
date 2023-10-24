from source.identifier.identifier import Identifier

def test_validar_entrada_caso_valido():
    identificacao = Identifier("ID", "A12345")
    resultado = identificacao.validar_entrada()
    assert resultado == "Válido"

def test_validar_entrada_caso_invalido_letra_inicial():
    identificacao = Identifier("ID", "12345A")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"

def test_validar_entrada_caso_invalido_comprimento():
    identificacao = Identifier("ID", "AB123456")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"

def test_validar_entrada_caso_invalido_em_branco():
    identificacao = Identifier("ID", "")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"

def test_validar_entrada_caso_invalido_caracter_especial():
    identificacao = Identifier("ID", "A@1234")
    resultado = identificacao.validar_entrada()
    assert resultado == "Inválido"
