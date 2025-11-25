import os

MENU_PRINCIPAL = """Menu Principal
1 | Relatórios
2 | Inserir Registros
3 | Atualizar Registros
4 | Remover Registros
5 | Sair
"""

MENU_RELATORIOS = """Relatórios
1 | Relatório de Funcionários
2 | Relatório de Movimentação de Estoque
3 | Relatório de Produtos por Fornecedor
4 | Relatório de Produtos
5 | Relatório de Fornecedores 
0 | Sair
"""

MENU_ENTIDADES = """Entidades
1 | Produtoos
2 | Fornecedores
3 | Funcionarios
4 | Movimentacoes Estoque
5 | Produtos Fornecedores
"""

def limpar_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")