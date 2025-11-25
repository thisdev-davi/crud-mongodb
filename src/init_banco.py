from conexion.conexao_mongo import ConexaoMongo
from pymongo import ASCENDING

def reset_banco():
    mongo = ConexaoMongo()
    mongo.connect()

    colecoes = ["movimentacoes_estoque", "produtos_fornecedores", "fornecedores", "funcionarios", "produtos"]

    for c in colecoes:
        mongo.db.drop_collection(c)
        print(f"Coleção {c} excluida.")
    print()

    for c in colecoes:
        mongo.db.create_collection(c)
        print(f"Coleção {c} criada.")
    print()

    mongo.db["produtos"].create_index([("codigo_barras", ASCENDING)], unique=True)
    mongo.db["fornecedores"].create_index([("cnpj", ASCENDING)], unique=True)
    mongo.db["funcionarios"].create_index([("cpf", ASCENDING)], unique=True)
    mongo.db["produtos_fornecedores"].create_index([("produtos_id", ASCENDING), ("fornecedores_id", ASCENDING)], unique=True)
    print("Uniques criados.")
    print()

    print("Banco pronto para uso.")

if __name__ == "__main__":
    reset_banco()