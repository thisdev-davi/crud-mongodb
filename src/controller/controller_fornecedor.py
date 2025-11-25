from src.model.fornecedores import Fornecedor
from src.conexion.conexao_mongo import ConexaoMongo
from src.repository.repository_fornecedor import RepositoryFornecedor
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerFornecedor:
    def __init__(self):
        self.mongo = ConexaoMongo()
        self.repository_fornecedor = RepositoryFornecedor()

    def inserir_fornecedor(self):
        self.mongo.connect()
        while True:
            if not Relatorio().get_relatorio_fornecedores():
                print()

            cnpj = input("Cnpj do fornecedor novo: ")
            if not self.repository_fornecedor.existencia_fornecedor(self.mongo, cnpj):
                nome = input("Nome do fornecedor: ")
                telefone = input("Telefone do fornecedor: ")
        
                fornecedor: Fornecedor = self.repository_fornecedor.inserir_fornecedor(self.mongo, Fornecedor(cnpj, nome, telefone))
                if fornecedor:
                    print(f"{fornecedor} cadastrado.")

                    if validar_continuacao("Deseja continuar inserindo registros?"):
                        limpar_console()
                    else:
                        limpar_console()
                        break
                else:
                    print("Erro ao cadastrar o fornecedor!")
            else:
                print("Cnpj já cadastrado!")
                if not validar_continuacao("Deseja continuar inserindo registros?"):
                        break

            print()
        self.mongo.close()
        return False

    def excluir_fornecedor(self):
        self.mongo.connect()

        # se não tiverem registros
        if not Relatorio().get_relatorio_fornecedores():
            print("Não há fornecedores cadastrados")
            input("Aperte enter para sair...")
            self.mongo.close()
            return

        cnpj = input("Cnpj do fornecedor a ser excluído: ")
        if self.repository_fornecedor.existencia_fornecedor(self.mongo, cnpj):

            fornecedor: Fornecedor = self.repository_fornecedor.buscar_fornecedor(self.mongo, cnpj)
            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_fornecedor.excluir_fornecedor(self.mongo, cnpj)
                
                if excluido:
                    limpar_console()
                    print(f"{fornecedor} excluído.")
                else:
                    print("Fornecedor não pode ser excluído!")
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("Cnpj não encontrado!")

        print()
        self.mongo.close()


    def atualizar_fornecedor(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_fornecedores():
            print("não há fornecedores cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        cnpj = input("Cnpj do fornecedor para atualização: ")
        if self.repository_fornecedor.existencia_fornecedor(self.mongo, cnpj):
            nome = input("Nome novo do fornecedor: ")
            telefone = input("Telefone novo do fornecedor: ")
            
            fornecedor_antigo = self.repository_fornecedor.buscar_fornecedor(self.mongo, cnpj)
            self.repository_fornecedor.atualizar_fornecedor(self.mongo, Fornecedor(cnpj, nome, telefone))
            fornecedor_novo = self.repository_fornecedor.buscar_fornecedor(self.mongo, cnpj)

            if fornecedor_antigo != fornecedor_novo:
                print(f"{fornecedor_antigo} atualizado.")

                if validar_continuacao("Deseja alterar mais registros?"):
                    limpar_console()
                    return True
            else:
                print("Erro ao atualizar o fornecedor!")
        else:
            print("Cnpj não encontrado!")
        
        print()
        self.mongo.close()
        return False
    
    def buscar_fornecedor(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_fornecedores():
            print("não há fornecedores cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        cnpj: str = input("Cnpj do fornecedor: ")
        fornecedor: Fornecedor = self.repository_fornecedor.buscar_fornecedor(self.mongo, cnpj)
            
        if fornecedor:
            print(fornecedor)
        else:
            print("Fornecedor não encontrado pelo Cnpj")

        self.mongo.close()