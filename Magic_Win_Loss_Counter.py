import pyautogui as pt
import keyboard
import time
import sys
import os
from rich import print
from rich.console import Console
from rich.table import Table
#----------------------------------------------------------------------------------

def caminho_arquivo(nome):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nome)
    return os.path.join(os.path.abspath("."), nome)

imagem_derrota = caminho_arquivo("imagem_derrota_magic.png")
imagem_vitoria = caminho_arquivo("imagem_vitoria_magic.png")

imagem_derrota = "imagem_derrota_magic.png"
imagem_vitoria = "imagem_vitoria_magic.png"

derrotas = 0
vitorias = 0

foi_derrotado = False
foi_vencedor = False

#----------------------------------------------------------------------------------

def procura_imagem_derrota():
    global derrotas, foi_derrotado
    
    if encontrou_imagem_derrota:
        #print("ACHEI TUA DERROTA KKKKK!!!")
        if not foi_derrotado:
            derrotas += 1
            foi_derrotado = True
            print(f"[red][+]Derrota detectada! Total de derrotas: {derrotas}[/red]")
    else:
        foi_derrotado = False
        #print("[red]NÃO ACHEI A IMAGEM DE DERROTA!![/red]")
        
def procura_imagem_vitoria():
    global vitorias, foi_vencedor
    
    if encontrou_imagem_vitoria:
        #print("ACHEI A SUA VITORIA!!!")
        if not foi_vencedor:
            vitorias += 1
            foi_vencedor = True
            print(f"[bold green][+]Vitória detectada! Total de vitórias: {vitorias}[/bold green]")
    else:
        foi_vencedor = False
        #print("[red]NÃO ACHEI A IMAGEM DE VITORIA!![/red]")

#----------------------------------------------------------------------------------
while True:
    if keyboard.is_pressed("q"):
        break
    try:
        encontrou_imagem_derrota = pt.locateOnScreen(imagem_derrota, confidence=0.8)
    except pt.ImageNotFoundException:
        encontrou_imagem_derrota = None
        
    try:
        encontrou_imagem_vitoria = pt.locateOnScreen(imagem_vitoria, confidence=0.8)
    except pt.ImageNotFoundException:
        encontrou_imagem_vitoria = None
    
    procura_imagem_derrota()
    
    procura_imagem_vitoria()
    
    
    time.sleep(0.5)
#----------------------------------------------------------------------------------

tabela = Table(title="Contagem de Vitórias e Derrotas")

tabela.add_column("Resultado", style="cyan", justify="center")
tabela.add_column("Quantidade", style="magenta", justify="center")

tabela.add_row("Vitórias", str(vitorias))
tabela.add_row("Derrotas", str(derrotas))

console = Console()
console.print(tabela)