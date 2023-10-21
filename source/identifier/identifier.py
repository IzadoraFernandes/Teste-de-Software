import re

class Identifier:
    def __init__(self, id, elem):
        self.elem = elem
        self.id = id
        
    def validar_entrada(self):
        if re.match(r"^[a-zA-Z]\d{0,5}$", self.elem):
            return "Válido"
        else:
            return "Inválido"
        
    def __str__(self):
        return f"ID: {self.id}, Elemento: {self.elem}"

    

