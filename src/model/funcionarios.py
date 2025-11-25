
class Funcionario:
    def __init__(self, CPF:str=None, nome:str=None, telefone:str=None):
        self._CPF = CPF
        self.nome = nome
        self.telefone = telefone
    
    def get_cpf(self):
        return self._CPF
    
    def get_nome(self):
        return self.nome
    
    def get_telefone(self):
        return self.telefone
    
    def set_cpf(self, CPF:str):
        self._CPF = CPF

    def set_nome(self, nome:str):
        self.nome = nome

    def set_telefone(self, telefone:str):
        self.telefone = telefone

    def __str__(self):
        return f"Funcionario: {self.nome}, CPF: {self._CPF}, Telefone: {self.telefone}"
