from src.views.view_adicionar import view_adicionar
from src.views.view_buscar import view_buscar
from src.views.view_remover import view_remover
from src.views.view_alterar import view_alterar
from src.views.view_relatorio import view_relatorio

from src.utils.config import limpar_console
import time


def principal_menu():
    time.sleep(1)
    
    print("--------------------")
    print(" MENU PRINCIPAL\n")
    print("1  | ADICIONAR")
    print("2  | BUSCAR")
    print("3  | REMOVER")
    print("4  | ATUALIZAR")
    print("5  | RELATÓRIOS")
    print("6  | SAIR")

    try:
        opcao = int(input("-> "))
        limpar_console()
        
    
    except ValueError:
        print("Insira um valor válido!")
        print()
        return False

    if opcao == 1:
        view_adicionar()
    elif opcao == 2:
        view_buscar()
        
    elif opcao == 3:
        view_remover()

    elif opcao == 4:
        view_alterar()
    
    elif opcao == 5:
        view_relatorio()
    
    elif opcao == 6:
        return True
    
    else:
        print("Insira uma opção válida!")
        return False