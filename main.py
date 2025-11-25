from src.model.produtos import Produto
from src.views.view_principal import principal_menu
from src.utils.config import limpar_console
from src.utils.splash_screen import SplashScreen
import time

sair = False

limpar_console()

print(SplashScreen().get_updated_screen())
while not sair:
    sair = principal_menu()

limpar_console()

print("\n\n\n                                                       Fechando, adeus!")
print(SplashScreen().get_updated_screen())
time.sleep(5)