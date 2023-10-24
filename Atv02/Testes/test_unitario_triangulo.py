from src.triangulo.triangulo_funcoes import Triangulo
import pytest

def test_validar_todos_lados_zero():
    triangulo = Triangulo()
    triangulo.verificar(1,2,3)
    resultado = triangulo.verificar(1,2,3)
    assert resultado == False

def test_validar_lados_igual():
    triangulo = Triangulo()
    triangulo.verificar(1,2,3) 
    resultado = triangulo.verificar(1,2,3)
    assert resultado == True
    
def test_nenhum_lado_pode_ser_zero():
    triangulo = Triangulo()
    triangulo.verificar(1,2,3)
    resultado = triangulo.verificar(1,2,3)
    assert resultado == True
    
def test_cada_lado_ser_menor_soma_todos_lados_dividido_por_dois():
    triangulo = Triangulo()
    triangulo.verificar(1,2,3)
    resultado = triangulo.verificar(1,2,3)
    assert resultado == True

