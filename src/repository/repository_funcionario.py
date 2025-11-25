from src.conexion.conexao_mongo import ConexaoMongo
from src.model.funcionarios import Funcionario
import pandas as pd

class RepositoryFuncionario():
    def __init__(self):
        pass

    def buscar_funcionario(self, mongo: ConexaoMongo, cpf: str) -> Funcionario:
        dados_funcionario = mongo.db["funcionarios"].find_one({"cpf": cpf}, {"cpf": 1, "nome": 1, "telefone": 1, "_id": 0})
        
        if dados_funcionario:
            funcionario = Funcionario(dados_funcionario["cpf"], dados_funcionario["nome"], dados_funcionario["telefone"])
            return funcionario
        return None

    def inserir_funcionario(self, mongo: ConexaoMongo, funcionario: Funcionario) -> Funcionario:
        dados_funcionario = mongo.db["funcionarios"].insert_one({"cpf": funcionario.get_cpf(), "nome": funcionario.get_nome(), "telefone": funcionario.get_telefone()})

        if dados_funcionario:
            return funcionario
        return None 
    
    def excluir_funcionario(self, mongo: ConexaoMongo, cpf: str) -> bool:
        resultado = mongo.db["funcionarios"].delete_one({"cpf": cpf})
        return resultado.deleted_count > 0
           
    def atualizar_funcionario(self, mongo: ConexaoMongo, funcionario: Funcionario):
        mongo.db["funcionarios"].update_one({"cpf": funcionario.get_cpf()}, {"$set": {"nome": funcionario.get_nome(), "telefone": funcionario.get_telefone()}})
    
    def existencia_funcionario(self, mongo: ConexaoMongo, cpf : str) -> bool:
        df_funcionario = pd.DataFrame(list(mongo.db["funcionarios"].find({"cpf": cpf}, {"cpf": 1, "_id": 0})))

        return not df_funcionario.empty