from src.repository.repository_produto import RepositoryProduto
from src.repository.repository_fornecedor import RepositoryFornecedor
from src.repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.conexion.conexao_mongo import ConexaoMongo
from src.model.produtos_fornecedores import ProdutoFornecedor
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerProdutoFornecedor:
    def __init__ (self):
        self.mongo = ConexaoMongo()
        self.repository_produto = RepositoryProduto()
        self.repository_fornecedor = RepositoryFornecedor()
        self.repository_produto_fornecedor = RepositoryProdutoFornecedores()

    def inserir_produto_fornecedor(self):
        self.mongo.connect()
        while True:
            if not Relatorio().get_relatorio_produtos_fornecedores():
                print()

            if not Relatorio().get_relatorio_produtos():
                print("não há produtos cadastrados")
                input("aperte enter para sair...")
                break

            id_produto = input("Id do produto: ")
            produto = self.repository_produto.buscar_produto(self.mongo, id_produto)
            if not produto:
                print("Produto não encontrado!")
                print()
                continue
        
            if not Relatorio().get_relatorio_fornecedores():
                print("não há fornecedores cadastrados")
                input("aperte enter para sair...")
                continue

            cnpj = input("Cnpj do fornecedor: ")
            fornecedor = self.repository_fornecedor.buscar_fornecedor(self.mongo, cnpj)
            if not fornecedor:
                print("Fornecedor não cadastrado!")
                print()
                continue

            produto_fornecedor: ProdutoFornecedor = self.repository_produto_fornecedor.inserir_produto_fornecedor(self.mongo, produto, fornecedor)
            if produto_fornecedor:
                print(f"Produto_fornecedor com id {produto_fornecedor.get_id()} cadastrado.")

                if validar_continuacao("Deseja continuar inserindo registros?"):
                    limpar_console()
                else:
                    limpar_console()
                    break
            else:
                print("Erro ao inserir a produto_fornecedor!")
                if not validar_continuacao("Deseja continuar inserindo registros?"):
                    limpar_console()
                    break
        
        print()
        self.mongo.close()
        return False
    
    def excluir_produto_fornecedor(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_produtos_fornecedores(): 
            print("não há produtos_fornecedores cadastrados")         
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("Id do produto_fornecedor a ser excluído: ")
        if self.repository_produto_fornecedor.existencia_produto_fornecedor(self.mongo, id):
            
            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_produto_fornecedor.excluir_produto_fornecedor(self.mongo, id)
            
                if excluido:
                    print(f"Produto_fornecedor com id {id} excluído.")
                else:
                    print("Produto_fornecedor não pode ser excluído!")
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("Id não encontrado!")
        
        print()
        self.mongo.close()

    def atualizar_produto_fornecedor(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_produtos_fornecedores():
            print("não há produtos_fornecedores cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("Id da associação produto_fornecedor para atualização: ")
        if self.repository_produto_fornecedor.existencia_produto_fornecedor(self.mongo, id):
            id_produto = input("Id do produto: ")
            produto = self.repository_produto.buscar_produto(self.mongo, id_produto)
            if not produto:
                print("produto não cadastrado!")
                input("aperte enter para sair...")
                self.mongo.close()
                return

            cnpj = input("cnpj do fornecedor: ")
            fornecedor = self.repository_fornecedor.buscar_fornecedor(self.mongo, cnpj)
            if not fornecedor:
                print("fornecedor não cadastrado!")
                input("aperte enter para sair...")
                self.mongo.close()
                return

            produto_fornecedor_antigo = ProdutoFornecedor(id, produto, fornecedor)
            self.repository_produto_fornecedor.atualizar_produto_fornecedor(self.mongo, produto_fornecedor_antigo)
            produto_fornecedor_novo: ProdutoFornecedor = self.repository_produto_fornecedor.buscar_produto_fornecedor(self.mongo, id)

            if produto_fornecedor_antigo != produto_fornecedor_novo:
                print(f"{produto_fornecedor_novo} atualizado.")

                if validar_continuacao("Deseja alterar mais registros?"):
                    limpar_console()
                    self.mongo.close()
                    return True
            else:
                print("Erro ao atualizar produto_fornecedor!")
        else:
            print("Id não encontrado!")
            return None
        
        print()
        self.mongo.close()
        return False
    
    def buscar_produto_fornecedor(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_produtos_fornecedores():
            print("não há produtos_fornecedores!")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("Id produto_fornecedor: ")
        produto_fornecedor: ProdutoFornecedor = self.repository_produto_fornecedor.buscar_produto_fornecedor(self.mongo, id)

        if produto_fornecedor:
            print(produto_fornecedor)
        else:
            print("Produto_fornecedor não encontrado para esse id!")
        
        print()
        self.mongo.close()