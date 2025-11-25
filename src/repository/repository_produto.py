from src.conexion.conexao_mongo import ConexaoMongo
from src.model.produtos import Produto
import pandas as pd
from bson.objectid import ObjectId

class RepositoryProduto():
    def __init__(self):
        pass
    
    def buscar_produto(self, mongo: ConexaoMongo, id: str) -> Produto:
        dados_produto = mongo.db["produtos"].find_one({"_id": ObjectId(id)}) 
        
        if dados_produto:
            return Produto(str(dados_produto["_id"]), dados_produto["nome"], dados_produto["preco_unitario"], dados_produto["descricao"], dados_produto["categoria"])
        return None

    def inserir_produto(self, mongo: ConexaoMongo, nome: str, preco: float, descricao: str, categoria: str) -> Produto:
        dados_produto = mongo.db["produtos"].insert_one({"nome": nome, "preco_unitario": preco, "descricao": descricao, "categoria": categoria})
        
        if dados_produto.inserted_id:
            id = dados_produto.inserted_id
            return Produto(str(id), nome, preco, descricao, categoria)
        return None

    def excluir_produto(self, mongo: ConexaoMongo, id: str) -> bool:
        id_obj = ObjectId(id)
        resultado = mongo.db["produtos"].delete_one({"_id": id_obj})

        return resultado.deleted_count > 0

    def atualizar_produto(self, mongo: ConexaoMongo, produto: Produto):
        mongo.db["produtos"].update_one({"_id": ObjectId(produto.get_id())}, 
        {"$set": {"nome": produto.get_nome(), "preco_unitario": produto.get_preco_unitario(), "descricao": produto.get_descricao(), "categoria": produto.get_categoria()}})

    def existencia_produto(self, mongo: ConexaoMongo, id: str) -> bool:
        df_produto = pd.DataFrame(list(mongo.db["produtos"].find({"_id": ObjectId(id)}, {"_id": 1})))
        return not df_produto.empty