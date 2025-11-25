from src.model.funcionarios import Funcionario
from src.conexion.conexao_mongo import ConexaoMongo
from src.repository.repository_funcionario import RepositoryFuncionario
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerFuncionario:
    def __init__(self):
        self.mongo = ConexaoMongo()
        self.repository_funcionario = RepositoryFuncionario()

    def inserir_funcionario(self):
        self.mongo.connect()
        while True:
            if not Relatorio().get_relatorio_funcionarios():
                print()

            cpf = input("Cpf do funcionário novo: ")
            if not self.repository_funcionario.existencia_funcionario(self.mongo, cpf):
                nome = input("Nome do funcionário: ")
                telefone = input("Telefone do funcionário: ")
            
                funcionarioInserido: Funcionario = self.repository_funcionario.inserir_funcionario(self.mongo, Funcionario(cpf, nome, telefone))
                if funcionarioInserido:
                    print(f"{funcionarioInserido} cadastrado.")

                    if validar_continuacao("Deseja continuar inserindo registros?"):
                        limpar_console()
                    else:
                        limpar_console()
                        break
                else:
                    print("Erro ao inserir o funcionário!")
            else:
                print("Cpf já cadastrado!")
                if not validar_continuacao("Deseja continuar inserindo registros?"):
                    break

            print()
        self.mongo.close()
        return False

    def excluir_funcionario(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_funcionarios():
            print("não há fornecedores cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        cpf = input("Cpf do funcionário a ser excluído: ")
        if self.repository_funcionario.existencia_funcionario(self.mongo, cpf):
            funcionario_excluido: Funcionario = self.repository_funcionario.buscar_funcionario(self.mongo, cpf)
            
            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_funcionario.excluir_funcionario(self.mongo, cpf)
                
                if excluido:
                    limpar_console()
                    print(f"{funcionario_excluido} excluído.")
                else:
                    print("Funcionário não pode ser excluído!\n**Está associado na tabela MOVIMENTACAO_ESTOQUE")
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("Cpf não encontrado!")

        print()
        self.mongo.close()
    
    def atualizar_funcionario(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_funcionarios():
            input("Aperte enter para sair...")
            self.mongo.close()
            return

        cpf = input("Cpf do funcionário para atualização: ")
        if self.repository_funcionario.existencia_funcionario(self.mongo, cpf):
            nome = input("Nome novo do funcionário: ")
            telefone = input("Telefone novo do funcionário: ")

            funcionario_atualizar = Funcionario(cpf, nome, telefone)
            self.repository_funcionario.atualizar_funcionario(self.mongo, funcionario_atualizar)
            print(f"{funcionario_atualizar} atualizado.")

            if validar_continuacao("Deseja alterar mais registros?"):
                limpar_console()
                return True
        else:
            print("Cpf não encontrado!")

        print()
        self.mongo.close()
        return False

    def buscar_funcionario(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_funcionarios():
                print("não há funcionários cadastrados!")
                input("aperte enter para sair...")
                self.mongo.close()
                return

        cpf = input("Cpf do funcionário: ")
        funcionario: Funcionario = self.repository_funcionario.buscar_funcionario(self.mongo, cpf)
        if funcionario:
            print(funcionario)
        else:
            print("Usuário não encontrado com este cpf!")

        print()
        self.mongo.close()