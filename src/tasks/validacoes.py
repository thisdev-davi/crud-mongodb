def validar_continuacao(mensagem: str) -> bool:
    validacao = input(str(mensagem + "\n(SIM/NAO)\n-> ")).upper().strip()
    
    return validacao == 'SIM' or validacao == 'S'

def validar_confirmacao(mensagem: str) -> bool:
    validacao = input(str(mensagem + "\n(SIM/NAO)\n-> ")).upper().strip()
    
    return validacao == 'SIM' or validacao == 'S'