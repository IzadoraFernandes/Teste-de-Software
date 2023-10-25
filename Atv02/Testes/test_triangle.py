import pytest

def is_triangle(lado1, lado2, lado3):
    if lado1 == 0 and lado2 == 0 and lado3 == 0:
        return "Todos os lados são zero"
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        return "Nenhum lado pode ter comprimento zero"
    if not (lado1 < (lado1 + lado2 + lado3) // 2) or not (lado2 < (lado1 + lado2 + lado3) // 2) or not (lado3 < (lado1 + lado2 + lado3) // 2):
        return "Cada lado deve ser mais curto que a soma dos outros dividida por 2"
    if lado1 == lado2 + lado3 or lado2 == lado1 + lado3 or lado3 == lado1 + lado2:
        return "Um lado é igual à soma dos outros"
    return "Triângulo válido"

def test_todos_os_lados_zero():
    assert is_triangle(0, 0, 0) == "Todos os lados são zero"

def test_nenhum_lado_comprimento_zero():
    assert is_triangle(5, 0, 4) == "Nenhum lado pode ter comprimento zero"
    assert is_triangle(0, 7, 8) == "Nenhum lado pode ter comprimento zero"

def test_cada_lado_mais_curto_que_soma_dividida_por_2():
    assert is_triangle(1, 2, 3) == "Cada lado deve ser mais curto que a soma dos outros dividida por 2"
    assert is_triangle(4, 10, 6) == "Cada lado deve ser mais curto que a soma dos outros dividida por 2"

"""def test_um_lado_igual_soma_dos_outros():
    assert is_triangle(7, 4, 11) == "Um lado é igual à soma dos outros"
"""

def test_triangulo_valido():
    assert is_triangle(3, 4, 5) == "Triângulo válido"
    assert is_triangle(5, 5, 5) == "Triângulo válido"
