from src.conexion.conexao_mongo import ConexaoMongo
import pandas as pd

class Relatorio:
    def __init__(self):
        self.mongo = ConexaoMongo()

    def get_relatorio_produtos(self):
        self.mongo.connect()
        print("listagem produtos")
        print("--------------------------------------------------")
        print()

        relatorio = self.mongo.db["produtos"].find({}, {"_id": 1, "nome": 1, "preco_unitario": 1, "descricao": 1, "categoria": 1}).sort([("categoria", 1), ("preco_unitario", 1)])
        lista = list(relatorio)

        if not lista:
            print("não há produtos\n")
            self.mongo.close()
            return False
        else:
            for produto in lista:
                produto["_id"] = str(produto["_id"])

            df = pd.DataFrame(lista)
            print(df.to_string(index=False))
            print()

            self.mongo.close()
            return True

    def get_relatorio_fornecedores(self):
        self.mongo.connect()
        print("listagem fornecedores")
        print("--------------------------------------------------")
        print()

        relatorio = self.mongo.db["fornecedores"].find({}, {"cnpj": 1, "nome": 1, "telefone": 1}).sort([("nome", 1)])
        lista = list(relatorio)

        if not lista:
            print("não há fornecedores\n")
            self.mongo.close()
            return False
        
        df = pd.DataFrame(lista)
        print(df.to_string(index=False))
        print()

        self.mongo.close()
        return True

    def get_relatorio_funcionarios(self):
        self.mongo.connect()
        print("listagem funcionários")
        print("--------------------------------------------------")
        print()

        relatorio = self.mongo.db["funcionarios"].find({}, {"cpf": 1, "nome": 1, "telefone": 1}).sort([("nome", 1)])
        lista = list(relatorio)

        if not lista:
            print("não há funcionários\n")
            self.mongo.close()
            return False
        
        df = pd.DataFrame(lista)
        print(df.to_string(index=False))
        print()

        self.mongo.close()
        return True

    def get_relatorio_produtos_fornecedores(self):
        self.mongo.connect()
        print("listagem produtos_fornecedores")
        print("--------------------------------------------------")
        print()

        pipeline = [
            { 
                "$addFields": {"id_produto" : { "$toObjectId": "$id_produto"} } 
            },
            {
                "$lookup":{
                    "from": "produtos",
                    "localField": "id_produto",
                    "foreignField": "_id",
                    "as": "dados_produto"
                }
            },
            { "$unwind": "$dados_produto" },
            {
                "$lookup": {
                    "from": "fornecedores",
                    "localField": "cnpj_fornecedor",
                    "foreignField": "cnpj",
                    "as": "dados_fornecedor"
                }
            },
            { "$unwind": "$dados_fornecedor" },
            {
                "$project": {
                    "_id": 0,
                    "id_associacao": { "$toString": "$_id"},
                    "nome_produto" : "$dados_produto.nome",
                    "nome_fornecedor": "$dados_fornecedor.nome",
                    "cnpj_fornecedor": 1
                }
            },
            {
                "$sort": {"nome_fornecedor": -1}
            }
        ]
        resultado = self.mongo.db["produtos_fornecedores"].aggregate(pipeline)
        lista = list(resultado)

        if not lista:
            print("não há produtos_fornecedores\n")
            self.mongo.close()
            return False

        df = pd.DataFrame(lista)
        colunas = ["id_associacao", "nome_produto", "nome_fornecedor", "cnpj_fornecedor"]
        df = df[colunas]
        print(df.to_string(index=False))

        print()
        self.mongo.close()
        return True
    
    def get_relatorio_movimentacoes(self):
        self.mongo.connect()
        print("listagem movimentações de estoque")
        print("--------------------------------------------------")
        print()

        pipeline = [
            {
                "$lookup":{
                    "from": "funcionarios",
                    "localField": "cpf_funcionario",
                    "foreignField": "cpf",
                    "as": "dados_funcionario"
                }
            },
            { "$unwind": "$dados_funcionario" },
            {
                "$addFields": {
                    "id_obj": { "$toObjectId": "$id_produto_fornecedor" }
                }
            },
            {
                "$lookup": {
                    "from": "produtos_fornecedores",
                    "localField": "id_obj",
                    "foreignField": "_id",
                    "as": "dados_vinculo"
                }
            },
            { "$unwind": "$dados_vinculo" },
            {
                "$lookup": {
                    "from": "fornecedores",
                    "localField": "dados_vinculo.cnpj_fornecedor",
                    "foreignField": "cnpj",
                    "as": "dados_fornecedor"
                }
            },
            { "$unwind": "$dados_fornecedor" },
            {
                "$addFields": {
                    "id_produto_obj": {"$toObjectId": "$dados_vinculo.id_produto"}
                }
            },
            {
                "$lookup": {
                    "from": "produtos",
                    "localField": "id_produto_obj",
                    "foreignField": "_id",
                    "as": "dados_produto"
                }
            },
            { "$unwind": "$dados_produto" },
            {
                "$project": {
                    "_id": 0,
                    "id_movimentacao": { "$toString": "$_id"},
                    "data_movimentacao": 1,
                    "tipo_movimentacao": 1,
                    "nome_produto": "$dados_produto.nome",
                    "quantidade": 1,
                    "cpf_funcionario": "$dados_funcionario.cpf",
                    "cnpj_fornecedor": "$dados_fornecedor.cnpj"
                }
            },
            { "$sort": {"tipo_movimentacao": 1, "data_movimentacao": 1} }
        ]
        resultado = self.mongo.db["movimentacoes_estoque"].aggregate(pipeline)
        lista = list(resultado)

        if not lista:
            print("não há movimentações de estoque\n")
            self.mongo.close()
            return False
        
        df = pd.DataFrame(lista)
        colunas = ["id_movimentacao", "data_movimentacao", "tipo_movimentacao", "nome_produto", "quantidade", "cpf_funcionario", "cnpj_fornecedor"]
        df = df[colunas]

        print(df.to_string(index=False))
        print()

        self.mongo.close()
        return True