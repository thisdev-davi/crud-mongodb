from src.repository.repository_funcionario import RepositoryFuncionario
from src.repository.repository_produto_fornecedores import RepositoryProdutoFornecedores
from src.repository.repository_movimentacao_estoque import RepositoryMovimentacaoEstoque
from src.conexion.conexao_mongo import ConexaoMongo
from datetime import date
from src.tasks.validacoes import validar_confirmacao, validar_continuacao
from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

class ControllerMovimentacaoEstoque:
    def __init__(self):
        self.mongo = ConexaoMongo()
        self.repository_produto_fornecedores = RepositoryProdutoFornecedores()
        self.repository_funcionario = RepositoryFuncionario()
        self.repository_movimentacao_estoque = RepositoryMovimentacaoEstoque()

    def inserir_movimentacao_estoque(self):
        self.mongo.connect()
        try:
            while True:
                if not Relatorio().get_relatorio_movimentacoes():
                    print()

                if not Relatorio().get_relatorio_produtos_fornecedores():
                    print("não há produtos_fornecedores cadastrados")
                    input("aperte enter para sair...")
                    break
                
                id_produto_fornecedor = input("Id da associação produto_fornecedor: ")
                produto_fornecedor = self.repository_produto_fornecedores.buscar_produto_fornecedor(self.mongo, id_produto_fornecedor)
                if not produto_fornecedor:
                    print("Associação produto_fornecedor não cadastrada!")
                    print()
                    continue

                if not Relatorio().get_relatorio_funcionarios():
                    print("não há funcionarios cadastrados")
                    input("aperte enter para sair...")
                    break

                cpf_funcionario = input("cpf do funcionário: ")
                funcionario = self.repository_funcionario.buscar_funcionario(self.mongo, cpf_funcionario)
                if not funcionario:
                    print("Funcionário não cadastrado!")
                    continue

                quantidade = int(input("Quantidade: "))
                tipo_movimentacao = input("Tipo de movimentação (ENTRADA, SAÍDA): ")
                if tipo_movimentacao not in ["ENTRADA", "SAÍDA", "SAIDA"]:
                    print("Tipo de movimentação inválido! use 'ENTRADA' ou 'SAÍDA'.")
                    continue
            
                data_atual = date.today().isoformat()
                movimentacao_estoque = self.repository_movimentacao_estoque.inserir_movimentacao_estoque(self.mongo, produto_fornecedor, funcionario, quantidade, tipo_movimentacao, data_atual)

                if movimentacao_estoque:
                    print(f"Movimentação de estoque com id {movimentacao_estoque.get_id()} cadastrada.")
                    if validar_continuacao("Deseja continuar inserindo registros?"):
                        limpar_console()
                    else:
                        limpar_console()
                        break
                else:
                    print("Erro ao cadastrar!")
                    if not validar_continuacao("Deseja continuar inserindo registros?"):
                        limpar_console()
                        break
        except ValueError:
            print("Quantidade inválida!")
        except Exception as e:
            print(e)
        
        print()
        self.mongo.close()
        return False
        
    def excluir_movimentacao_estoque(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_movimentacoes():
            print("não há fornecedores cadastrados")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("Id da movimentação de estoque a ser excluída: ")
        if self.repository_movimentacao_estoque.existencia_movimentacao_estoque(self.mongo, id):
            if validar_confirmacao("Deseja realmente excluir este registro?"):
                excluido: bool = self.repository_movimentacao_estoque.excluir_movimentacao_estoque(self.mongo, id)

                if excluido:
                    limpar_console()
                    print("Movimentação excluída com sucesso.")
                else:
                    limpar_console()
                    print("Erro ao excluir a movimentação de estoque!")
            else:
                print("Remoção cancelada pelo usuário.")
        else:
            print("Id não encontrado!")

        self.mongo.close()
        print()
    
    def buscar_movimentacao_estoque(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_movimentacoes():
            print("não há movimentações no estoque!")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        id = input("Id da movimentação de estoque: ")
        movimentacao_estoque = self.repository_movimentacao_estoque.buscar_movimentacao_estoque(self.mongo, id)

        if movimentacao_estoque:
            print(movimentacao_estoque)
        else:
            print("Movimentação não encontrada com este id!")

        print()
        self.mongo.close()

    def atualizar_movimentacao_estoque(self):
        self.mongo.connect()

        if not Relatorio().get_relatorio_movimentacoes():
            print("não há movimentação de estoque")
            input("aperte enter para sair...")
            self.mongo.close()
            return

        try:
            id = input("Id da movimentação de estoque para atualização: ")
            if self.repository_movimentacao_estoque.existencia_movimentacao_estoque(self.mongo, id):
                quantidade = int(input("Quantidade nova: "))
                tipo_movimentacao = input("Tipo de movimentação nova (ENTRADA, SAÍDA): ")
                if tipo_movimentacao not in ["ENTRADA", "SAÍDA", "SAIDA"]:
                    print("Tipo de movimentação inválido! use 'ENTRADA' ou 'SAÍDA'.")
                    self.mongo.close()
                    return
                
                movimentacao = self.repository_movimentacao_estoque.buscar_movimentacao_estoque(self.mongo, id)
                movimentacao.set_quantidade(quantidade)
                movimentacao.set_tipo(tipo_movimentacao)

                self.repository_movimentacao_estoque.atualizar_movimentacao_estoque(self.mongo, movimentacao)
                
                print(f"Movimentacao com id {id} atualizado.")
                if validar_continuacao("Deseja alterar mais registros?"):
                    limpar_console()
                    self.mongo.close()
                    return
            else:
                print("Id não encontrado!")
        except ValueError:
            print("Quantidade inválida!")
        except Exception as e:
            print(e)
        
        print()
        self.mongo.close()
        return False