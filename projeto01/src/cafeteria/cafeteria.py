class Cafeteria:
    def __init__(self):
        self.cafe = 0 
        self.leite = 0
        self.acucar = 0
        self.dinheiro = 0 
        
    def add_cafe(self, quantidade):
        self.cafe += quantidade
        
    def add_leite(self, quantidade):
        self.leite += quantidade
        
    def add_acucar(self, quantidade):
        self.acucar += quantidade
        
    def add_dinheiro(self, valor):
        self.dinheiro += valor
        
    def get_total(self):
        return (self.cafe + self.leite + self.acucar) * self.dinheiro / 100
    
    def fazer_cafe(self, receita):
        if (
            self.cafe >= receita.cafe
            and self.leite >= receita.leite
            and self.acucar >= receita.acucar
            and self.dinheiro >= receita.custo  
        ):
            print("Fazendo o cafe")
            self.add_cafe(-receita.cafe)  
            self.add_leite(-receita.leite)
            self.add_acucar(-receita.acucar)
            self.add_dinheiro(-receita.custo) 
            return "Fazendo o cafe"  
        else:
            return "Não tem dinheiro ou ingredientes"

     
class Receita:
    def __init__(self, nome, cafe, leite, acucar, custo):
        self.nome = nome
        self.cafe = cafe
        self.leite = leite
        self.acucar = acucar
        self.custo = custo
        
    """def calcular_preco(self):
        preco = self.cafe + self.leite + self.acucar
        if preco < self.custo:
            print("O preço da receita é menor que o custo.")
        else:
            print("o preço da receita é maior que o custo. ") """