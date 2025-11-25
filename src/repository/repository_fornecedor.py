from src.conexion.conexao_mongo import ConexaoMongo
from src.model.fornecedores import Fornecedor
import pandas as pd

class RepositoryFornecedor():
    def __init__(self):
        pass
    
    def buscar_fornecedor(self, mongo: ConexaoMongo, cnpj: str) -> Fornecedor:
        dados_fornecedor = mongo.db["fornecedores"].find_one({"cnpj": cnpj}, {"cnpj": 1, "nome": 1, "telefone": 1, "_id": 0})
        
        if dados_fornecedor:
            fornecedor = Fornecedor(dados_fornecedor["cnpj"], dados_fornecedor["nome"], dados_fornecedor["telefone"])
            return fornecedor
        return None

    def inserir_fornecedor(self, mongo: ConexaoMongo, fornecedor: Fornecedor) -> Fornecedor:
        dados_fornecedor = mongo.db["fornecedores"].insert_one({"cnpj": fornecedor.get_cnpj(), "nome": fornecedor.get_nome(), "telefone": fornecedor.get_telefone()})

        if dados_fornecedor:
            return fornecedor
        return None 
    
    def excluir_fornecedor(self, mongo: ConexaoMongo, cnpj: str) -> bool:
        resultado = mongo.db["fornecedores"].delete_one({"cnpj": cnpj})
        return resultado.deleted_count > 0
           
    def atualizar_fornecedor(self, mongo: ConexaoMongo, fornecedor: Fornecedor):
        mongo.db["fornecedores"].update_one({"cnpj": fornecedor.get_cnpj()}, {"$set": {"nome": fornecedor.get_nome(), "telefone": fornecedor.get_telefone()}})
    
    def existencia_fornecedor(self, mongo: ConexaoMongo, cnpj : str) -> bool:
        df_fornecedor = pd.DataFrame(list(mongo.db["fornecedores"].find({"cnpj": cnpj}, {"cnpj": 1, "_id": 0})))

        return not df_fornecedor.empty