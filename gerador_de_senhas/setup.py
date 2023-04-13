import sys
from cx_Freeze import setup, Executable #importação das bibliotecas

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}
#importação das ibliotecas necessárias para a execução da aplicação
base = None #configuração para aplicações de interface gráfica
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    #informações sobre a aplicação a ser gerado o executável
    name="Gerador de senhas",
    version="0.1",
    description="Gera senhas",
    options={"build_exe": build_exe_options},
    executables=[Executable("gerador_de_senhas.py", base=base)] #nome do arquivo da aplicação
)
