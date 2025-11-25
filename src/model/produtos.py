class Produto:
    def __init__(self, id:str=None, nome:str=None, preco_unitario:float=None, descricao:str=None, categoria:str=None):
        self._id = id
        self._nome = nome
        self._preco_unitario = preco_unitario
        self._descricao = descricao
        self._categoria = categoria

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_preco_unitario(self):
        return self._preco_unitario
    
    def get_descricao(self):
        return self._descricao
    
    def get_categoria(self):
        return self._categoria
    
    def set_id(self, id:str):
        self._id = id
    
    def set_nome(self, nome:str):
        self._nome = nome

    def set_preco_unitario(self, preco_unitario:float):
        self._preco_unitario = preco_unitario

    def set_descricao(self, descricao:str):
        self._descricao = descricao

    def set_categoria(self, categoria:str):
        self._categoria = categoria

    def __str__(self):
        return f"Produto: {self._nome} (ID: {self._id}), Preço Unitário: {self._preco_unitario}, Descrição: {self._descricao}, Categoria: {self._categoria}"