from src.conexion.conexao_mongo import ConexaoMongo
from src.model.produtos import Produto
from src.repository.repository_produto import RepositoryProduto
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerProduto:
    def __init__(self):
        self.mongo = ConexaoMongo()
        self.repository_produto = RepositoryProduto()

    def inserir_produto(self):
        self.mongo.connect()
        while True:
            if not Relatorio().get_relatorio_produtos():
                print()

            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            descricao = input("Descrição do produto: ")
            categoria = input("Categoria do produto (MOUSE, TECLADO, MONITOR, HEADSET, MOUSEPAD): ").upper().strip()

            if categoria not in ["MOUSE", "TECLADO", "MONITOR", "HEADSET", "MOUSEPAD"]:
                print("Categoria inválida -> (MOUSE, TECLADO, MONITOR, HEADSET, MOUSEPAD)")
                continue

            produto_cadastrado: Produto = self.repository_produto.inserir_produto(self.mongo, nome, preco, descricao, categoria)

            if produto_cadastrado:
                print(f"Produto cadastrado com ID {produto_cadastrado.get_id()}.")
                if validar_continuacao("Deseja continuar inserindo registros?"):
                    limpar_console()
                else:
                    limpar_console()
                    break
            else:
                print(f"Erro ao cadastrar o produto!")
                if not validar_continuacao("Deseja continuar inserindo registros?"):
                    limpar_console()
                    break
                
            print()
        self.mongo.close()
        return False

    def excluir_produto(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_produtos():
            print("não há produtos cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("id do produto a ser excluído: ")
        if self.repository_produto.existencia_produto(self.mongo, id):
            produto_excluido: Produto = self.repository_produto.buscar_produto(self.mongo, id)

            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_produto.excluir_produto(self.mongo, id)
                if excluido:
                    limpar_console()
                    print(f"{produto_excluido} excluído.")

                else:
                    limpar_console()
                    print("Produto não pode ser excluído!")  
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("Id não encontrado!")
        
        print()
        self.mongo.close()

    def atualizar_produto(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_produtos():
            print("não há produtos cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("Id do produto para atualização: ")
        if self.repository_produto.existencia_produto(self.mongo, id):
            nome = input("Nome novo do produto: ")
            preco = float(input("Preco novo do produto: "))
            descricao = input("Descricao nova do produto: ")
            categoria = input("Categoria nova do produto: ")
            
            produto_antigo = self.repository_produto.buscar_produto(self.mongo, id)
            self.repository_produto.atualizar_produto(self.mongo, Produto(id, nome, preco, descricao, categoria))
            produto_novo = self.repository_produto.buscar_produto(self.mongo, id)

            if produto_antigo != produto_novo:
                print(f"{produto_novo} atualizado.")

                if validar_continuacao("Deseja alterar mais registros?"):
                    limpar_console()
                    return True
            else:
                limpar_console()
                print("Erro ao atualizar o produto!")
        else:
            print("Id não encontrado!")

        print()
        self.mongo.close()
        return False
    
    def buscar_produto(self):
        self.mongo.connect()
        
        if not self.mongo.db["produtos"].find_one():
                print("não há produtos cadastrados!")
                input("aperte enter para sair...")
                self.mongo.close()
                return

        id = input("Id do produto: ")
        produto: Produto = self.repository_produto.buscar_produto(self.mongo, id)

        if produto:
            print(produto)
        else:
            print("Id não encontrado!")
            
        print()
        self.mongo.close()