from src.reports.relatorios import Relatorio
from src.utils.config import limpar_console

def view_relatorio():
    continuar = True

    while continuar:
        print("--------------------")
        print("RELATÓRIOS\n")
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
            Relatorio().get_relatorio_funcionarios()
        
        elif opcao == 2:
            Relatorio().get_relatorio_produtos()

        elif opcao == 3:
            Relatorio().get_relatorio_fornecedores()

        elif opcao == 4:
            Relatorio().get_relatorio_movimentacoes()

        elif opcao == 5:
            Relatorio().get_relatorio_produtos_fornecedores()

        elif opcao == 6:
            return False
        
        else:
            print("Insira uma opção válida!")
            return True