import pytest
from src.cafeteria.cafeteria import Cafeteria, Receita

#Receita
def test_receita():
    receita = Receita("Café com Leite", 1, 1, 1, 2)
    
    assert receita.nome == "Café com Leite"
    assert receita.cafe == 1
    assert receita.leite == 1
    assert receita.acucar == 1
    assert receita.custo == 2

#Cafeteria
def test_cafeteria():
    cafeteria = Cafeteria()
    receita = Receita("Café Preto", 1, 0, 0, 1)
    
    assert cafeteria.cafe == 0
    assert cafeteria.leite == 0
    assert cafeteria.acucar == 0
    assert cafeteria.dinheiro == 0
    
    cafeteria.add_cafe(3)
    cafeteria.add_leite(2)
    cafeteria.add_acucar(1)
    cafeteria.add_dinheiro(5)
    
    assert cafeteria.cafe == 3
    assert cafeteria.leite == 2
    assert cafeteria.acucar == 1
    assert cafeteria.dinheiro == 5
    
    total = cafeteria.get_total()
    assert total == (3 + 2 + 1) * 5 / 100
    
    resultado = cafeteria.fazer_cafe(receita)
    assert resultado == "Fazendo o cafe"
    
    assert cafeteria.cafe == 2
    assert cafeteria.leite == 1
    assert cafeteria.acucar == 0
    assert cafeteria.dinheiro == 4

#falta de ingredientes e dinheiro
def test_cafeteria_sem_ingredientes_ou_dinheiro():
    cafeteria = Cafeteria()
    receita = Receita("Café com Leite", 2, 2, 2, 10)
    
    resultado = cafeteria.fazer_cafe(receita)
    assert resultado == "Não tem dinheiro ou ingredientes"

if __name__ == "__main":
    pytest.main()
