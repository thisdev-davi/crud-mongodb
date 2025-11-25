
class Fornecedor:
    def __init__(self, CNPJ:str, nome:str, telefone:str):
        self._CNPJ = CNPJ
        self._nome = nome
        self._telefone = telefone

    def get_cnpj(self):
        return self._CNPJ
    
    def get_nome(self):
        return self._nome
    
    def get_telefone(self):
        return self._telefone

    def set_cnpj(self, CNPJ:str):
        self._CNPJ = CNPJ
        
    def set_nome(self, nome:str):
        self._nome = nome

    def set_telefone(self, telefone:str):
        self._telefone = telefone

    def __str__(self):
        return f"Fornecedor: {self._nome}, CNPJ: {self._CNPJ}, Telefone: {self._telefone}"
