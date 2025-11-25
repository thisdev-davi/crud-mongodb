from src.conexion.conexao_mongo import ConexaoMongo
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.repository.repository_funcionario import RepositoryFuncionario
from src.model.produtos import Produto
from src.model.funcionarios import Funcionario
from src.model.movimentacoes_estoque import MovimentacaoEstoque
import pandas as pd
from bson.objectid import ObjectId

class RepositoryMovimentacaoEstoque():

    def __init__(self):
        self.repository_produto_fornecedores = RepositoryProdutoFornecedores()
        self.repository_funcionario = RepositoryFuncionario()

    def inserir_movimentacao_estoque(self, mongo: ConexaoMongo, produto_fornecedor: ProdutoFornecedor, funcionario: Funcionario, quantidade, tipo_movimentacao, data_atual) -> MovimentacaoEstoque:
        dados = mongo.db["movimentacoes_estoque"].insert_one({
            "id_produto_fornecedor": produto_fornecedor.get_id(), "cpf_funcionario": funcionario.get_cpf(), "quantidade": quantidade, "tipo_movimentacao": tipo_movimentacao, "data_movimentacao": data_atual
            })
        
        if dados.inserted_id:
            id= dados.inserted_id
            return MovimentacaoEstoque(str(id), produto_fornecedor, funcionario, quantidade, tipo_movimentacao, data_atual)
        return None
        
    def buscar_movimentacao_estoque(self, mongo: ConexaoMongo, id: str) -> MovimentacaoEstoque:
        dados = mongo.db["movimentacoes_estoque"].find_one({"_id": ObjectId(id)})

        if dados:
            obj_produto_fornecedor = self.repository_produto_fornecedores.buscar_produto_fornecedor(mongo, dados["id_produto_fornecedor"])
            obj_funcionario = self.repository_funcionario.buscar_funcionario(mongo, dados["cpf_funcionario"])
            quantidade = dados["quantidade"]
            tipo_movimentacao = dados["tipo_movimentacao"]
            data_movimentacao = dados["data_movimentacao"]

            movimentacao_estoque = MovimentacaoEstoque(str(dados["_id"]), obj_produto_fornecedor, obj_funcionario, quantidade, tipo_movimentacao, data_movimentacao)

            return movimentacao_estoque
        return None

    def excluir_movimentacao_estoque(self, mongo: ConexaoMongo, id: str) -> bool:
        dados = mongo.db["movimentacoes_estoque"].delete_one({"_id": ObjectId(id)})
        return dados.deleted_count > 0

    def atualizar_movimentacao_estoque(self, mongo: ConexaoMongo, movimentacao_estoque: MovimentacaoEstoque): 
        mongo.db["movimentacoes_estoque"].update_one(
            {"_id": ObjectId(movimentacao_estoque.get_id())}, 
            {"$set": {
                "id_produto_fornecedor": movimentacao_estoque.get_produto_fornecedor().get_id(), "cpf_funcionario": movimentacao_estoque.get_funcionario().get_cpf(), 
                "quantidade": movimentacao_estoque.get_quantidade(), "tipo_movimentacao": movimentacao_estoque.get_tipo(), "data_movimentacao": movimentacao_estoque.get_data()}
            })

    def existencia_movimentacao_estoque(self, mongo: ConexaoMongo, id: str) -> bool:
        df = pd.DataFrame(list(mongo.db["movimentacoes_estoque"].find({"_id": ObjectId(id)}, {"_id": 1})))
        return not df.empty