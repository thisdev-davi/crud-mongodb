from src.conexion.conexao_mongo import ConexaoMongo

from src.utils import config

class SplashScreen:
    def __init__(self):
        self.mongo = ConexaoMongo()
        
    def get_total_fornecedores(self):
        self.mongo.connect()
        return self.mongo.db["fornecedores"].count_documents({})

    def get_total_funcionarios(self):
        self.mongo.connect()
        return self.mongo.db["funcionarios"].count_documents({})

    def get_total_movimentacoes_estoque(self):
        self.mongo.connect()
        return self.mongo.db["movimentacoes_estoque"].count_documents({})

    def get_total_produtos_fornecedores(self):
        self.mongo.connect()
        return self.mongo.db["produtos_fornecedores"].count_documents({})

    def get_total_produtos(self):
        self.mongo.connect()
        return self.mongo.db["produtos"].count_documents({})

    def get_updated_screen(self):
        largura = 70
        borda_linha = "#" * largura

        criadores = [
            "Arthur Pomarolli",
            "Davi de Souza",
            "Mauro Barros",
            "Pedro Augusto"
        ]
        professor = "Prof. M.Sc. Howard Roatti."
        disciplina = "Banco de dados"
        semestre = "2025/2"
        
        def format_line(content=""):
            return f"#{content.ljust(largura - 2)}#"
        
        criadores_str = ""
        for i, nome in enumerate(criadores):
            prefixo = "   Criado por: " if i == 0 else "               "
            criadores_str += format_line(f"{prefixo}{nome}") + "\n"
        criadores_str = criadores_str.rstrip("\n")

        return f"""
{borda_linha}
{format_line("Sistema de Estoque".center(largura - 2))}
{format_line()}
{format_line("   Total de Registros:")}
{format_line(f"   1 | Fornecedores:".ljust(30) + str(self.get_total_fornecedores()).rjust(5))}
{format_line(f"   2 | Funcionarios:".ljust(30) + str(self.get_total_funcionarios()).rjust(5))}
{format_line(f"   3 | Mov. Estoque:".ljust(30) + str(self.get_total_movimentacoes_estoque()).rjust(5))}
{format_line(f"   4 | Prod. Fornecedores:".ljust(30) + str(self.get_total_produtos_fornecedores()).rjust(5))}
{format_line(f"   5 | Produtos:".ljust(30) + str(self.get_total_produtos()).rjust(5))}
{format_line()}
{format_line("   Dados do Grupo:")}
{format_line()}
{criadores_str}
{format_line()}
{format_line(f"   Professor:".ljust(15) + professor)}
{format_line()}
{format_line(f"   Disciplina:".ljust(15) + disciplina)}
{format_line(f"   Semestre:".ljust(15) + semestre)}
{borda_linha}
    """