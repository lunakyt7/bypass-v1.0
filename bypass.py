import os
import time

# Cores ANSI
verde = "\033[92m"
vermelho = "\033[91m"
amarelo = "\033[93m"
reset = "\033[0m"
azul = "\033[94m"

# ASCII Art com "SPEED BYPASS"
titulo = f"""{verde}
 _                                       _   ___
| |__  _   _ _ __   __ _ ___ ___  __   _/ | / _  |
| '_ \| | | | '_ \ / _` / __/ __| \ \ / / || | | |
| |_) | |_| | |_) | (_| \__ \__ \  \ V /| || |_| |
|_.__/ \__, | .__/ \__,_|___/___/   \_/ |_(_)___/
       |___/|_|

{reset}"""

# Respostas do bot
respostas = {
    "ativar": f"{verde}Bypass ativo com sucesso. Reinicie seu aparelho.{reset}",
    "limpar": f"{amarelo}Logs do cheat limpada com sucesso.{reset}",
    "key": f"{azul}Voce está usando o plano semanal, encerra em 7d {reset}",
}

# Lista de comandos disponíveis
comandos_disponiveis = f"""{amarelo}
Comandos disponíveis:
 ├── ativar     → Ativa o bypass
 ├── limpar     → Limpa os logs do cheat
 ├── key        → Mostra qual o seu plano
 └── sair       → Encerra o bypass
{reset}"""

def limpar_tela():
    os.system("clear" if os.name == "posix" else "cls")

def main():
    limpar_tela()
    print(titulo)
    print(comandos_disponiveis)
    print(f"{verde}BYPASS INJETADO. DIGITE 'sair' PARA ENCERRAR.{reset}\n")

    while True:
        entrada = input(f"{verde}$:{reset} ").lower().strip()
        if entrada == "sair":
