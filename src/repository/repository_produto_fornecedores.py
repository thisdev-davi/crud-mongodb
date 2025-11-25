from src.conexion.conexao_mongo import ConexaoMongo
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.repository.repository_produto import RepositoryProduto
from src.repository.repository_fornecedor import RepositoryFornecedor
from src.model.produtos import Produto
from src.model.fornecedores import Fornecedor
import pandas as pd
from bson.objectid import ObjectId

class RepositoryProdutoFornecedores():
    def __init__(self):
        self.repository_produto = RepositoryProduto()
        self.repository_fornecedor = RepositoryFornecedor()

    def inserir_produto_fornecedor(self, mongo: ConexaoMongo, produto: Produto, fornecedor: Fornecedor) -> ProdutoFornecedor:
        dados = mongo.db["produtos_fornecedores"].insert_one({"id_produto": produto.get_id(), "cnpj_fornecedor": fornecedor.get_cnpj()})
        if dados.inserted_id:
            id = dados.inserted_id
            return ProdutoFornecedor(str(id), produto, fornecedor)
        else:
            return None

    def buscar_produto_fornecedor(self, mongo: ConexaoMongo, id: str) -> ProdutoFornecedor:
        dados = mongo.db["produtos_fornecedores"].find_one({"_id": ObjectId(id)})
        if dados:
            produto = self.repository_produto.buscar_produto(mongo, dados["id_produto"])
            fornecedor = self.repository_fornecedor.buscar_fornecedor(mongo, dados["cnpj_fornecedor"])

            if produto and fornecedor:
                return ProdutoFornecedor(str(dados["_id"]), produto, fornecedor)
        return None

    def excluir_produto_fornecedor(self, mongo: ConexaoMongo, id: str) -> bool:
        id_obj = ObjectId(id)
        resultado = mongo.db["produtos_fornecedores"].delete_one({"_id": id_obj})

        return resultado.deleted_count > 0

    def atualizar_produto_fornecedor(self, mongo: ConexaoMongo, produto_fornecedor: ProdutoFornecedor):
        mongo.db["produtos_fornecedores"].update_one({"_id": ObjectId(produto_fornecedor.get_id())},
        {"$set": {"cnpj_fornecedor": produto_fornecedor.get_fornecedor().get_cnpj(), "id_produto": produto_fornecedor.get_produto().get_id()}})

    def existencia_produto_fornecedor(self, mongo: ConexaoMongo, id: str) -> bool:
        df = pd.DataFrame(list(mongo.db["produtos_fornecedores"].find({"_id": ObjectId(id)}, {"_id": 1})))
        return not df.empty