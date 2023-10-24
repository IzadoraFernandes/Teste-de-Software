class Triangulo:
    def __init__(self):
        ...

    def todos_lados_zero(self, a, b, c):
        if a == 0 and b == 0 and c == 0:
            return True
        else:
            return False
        
    def nenhum_lado_pode_ser_zero(self, a, b, c):
        if a != 0 or b != 0 or c != 0:
            return True
        else:
            return False
        
    def cada_lado_ser_menor_soma_todos_lados_dividio_por_dois(self, a, b, c):
        soma_todos_lados = a + b + c
        if a <= soma_todos_lados/2 and b <= soma_todos_lados/2 and c <= soma_todos_lados/2:
            return True
        else:
            return False
    def lados_iguais(self, a, b, c):
        if a == b and b == c:
            return True
        else:
            return False
        
    def verificar(self, a, b, c):
        if self.cada_lado_ser_menor_soma_todos_lados_dividio_por_dois(a, b, c)  and self.lados_iguais(a, b, c) and self.nenhum_lado_pode_ser_zero(a, b, c):
            return True
        return False
        