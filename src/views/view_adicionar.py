from src.controller.controller_fornecedor import ControllerFornecedor
from src.controller.controller_funcionario import ControllerFuncionario
from src.controller.controller_produto import ControllerProduto
from src.controller.controller_produto_fornecedor import ControllerProdutoFornecedor
from src.controller.controller_movimentacao_estoque import ControllerMovimentacaoEstoque
from src.utils.config import limpar_console

def view_adicionar():
    continuar = True

    while continuar:
        print("--------------------")
        print(" MENU ADICIONAR\n")
        print("1 | FUNCIONÁRIOS")
        print("2 | PRODUTOS")
        print("3 | FORNECEDORES")
        print("4 | MOVIMENTAÇÕES")
        print("5 | PRODUTO FORNECEDOR")
        print("6 | VOLTAR AO MENU PRINCIPAL")

        try:
            opcao = int(input("-> "))
            limpar_console()
        
        except ValueError:
            print("Insira um valor válido!")
            print()
            return False
        
        if opcao == 1:
            continuar = ControllerFuncionario().inserir_funcionario()
        
        elif opcao == 2:
            continuar = ControllerProduto().inserir_produto()

        elif opcao == 3:
            continuar = ControllerFornecedor().inserir_fornecedor()

        elif opcao == 4:
            continuar = ControllerMovimentacaoEstoque().inserir_movimentacao_estoque()

        elif opcao == 5:
            continuar = ControllerProdutoFornecedor().inserir_produto_fornecedor()
        
        elif opcao == 6:
            return False
        
        else:
            print("Insira uma opção válida!")
            return True