from src.controller.controller_fornecedor import ControllerFornecedor
from src.controller.controller_funcionario import ControllerFuncionario
from src.controller.controller_produto import ControllerProduto
from src.controller.controller_produto_fornecedor import ControllerProdutoFornecedor
from src.controller.controller_movimentacao_estoque import ControllerMovimentacaoEstoque
from src.utils.config import limpar_console

def view_buscar():
    sair = False

    while not sair:
        print("--------------------")
        print(" MENU BUSCAR\n")
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
            ControllerFuncionario().buscar_funcionario()
        
        elif opcao == 2:
            ControllerProduto().buscar_produto()

        elif opcao == 3:
            ControllerFornecedor().buscar_fornecedor()

        elif opcao == 4:
            ControllerMovimentacaoEstoque().buscar_movimentacao_estoque()

        elif opcao == 5:
            ControllerProdutoFornecedor().buscar_produto_fornecedor()
        
        elif opcao == 6:
            return True
        
        else:
            print("Insira uma opção válida!")
            return False