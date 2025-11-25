from src.model.produtos_fornecedores import ProdutoFornecedor
from src.model.funcionarios import Funcionario
from datetime import date


class MovimentacaoEstoque:
    def __init__(self, id:str=None, produto_fornecedor:ProdutoFornecedor=None, funcionario:Funcionario=None, quantidade:int=0, tipo:str="", data:date=None):
        self._id = id
        self._produto_fornecedor = produto_fornecedor
        self._funcionario = funcionario
        self._quantidade = quantidade
        self._tipo = tipo
        self._data = data

    def get_id(self):
        return self._id
    
    def get_produto_fornecedor(self):
        return self._produto_fornecedor
    
    def get_funcionario(self):
        return self._funcionario
    
    def get_quantidade(self):
        return self._quantidade
    
    def get_tipo(self):
        return self._tipo

    def get_data(self):
        return self._data
    
    def set_id(self, id:str):
        self._id = id

    def set_produto_fornecedor(self, produto_fornecedor:ProdutoFornecedor):
        self._produto_fornecedor = produto_fornecedor

    def set_funcionario(self, funcionario:Funcionario):
        self._funcionario = funcionario

    def set_quantidade(self, quantidade:int):
        self._quantidade = quantidade

    def set_tipo(self, tipo:str):
        self._tipo = tipo

    def set_data(self, data:date):
        self._data = data

    def __str__(self):
        return f"Movimentacao Estoque: (ID: {self._id}), Produto/Fornecedor: [{self._produto_fornecedor}], Funcionario: [{self._funcionario}], Quantidade: {self._quantidade}, Tipo: {self._tipo}, Data: {self._data}"