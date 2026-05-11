import threading
import time
import keyboard
import pygame as pg

from choice_game import jogos
from win_loss_counter import WinLossCounter

# Inicializa o pygame aqui, na thread principal, antes de tudo
pg.mixer.init()
print("[Audio] pygame.mixer pronto.")

print("=" * 35)
print("      WIN LOSS COUNTER")
print("=" * 35)

# Mostrar jogos
for i, nome in enumerate(jogos.keys(), start=1):
    print(f"{i} - {nome}")

opcao = input("\nEscolha um jogo: ")

lista_jogos = list(jogos.keys())

# Verifica escolha
try:
    jogo_escolhido = lista_jogos[int(opcao) - 1]
except Exception:
    print("Opção inválida.")
    exit()

dados = jogos[jogo_escolhido]

# Cria contador
contador = WinLossCounter(
    dados["vitoria"],
    dados["derrota"]
)

# Thread de monitoramento
thread = threading.Thread(target=contador.iniciar)
thread.daemon = True
thread.start()

print(f"\nMonitorando {jogo_escolhido}...")
print("Pressione ESC para encerrar.\n")

ultimo_v = -1
ultimo_d = -1

# Loop principal
while True:

    # Atualiza placar apenas quando mudar
    if contador.vitorias != ultimo_v or contador.derrotas != ultimo_d:

        ultimo_v = contador.vitorias
        ultimo_d = contador.derrotas

        print("=" * 25)
        print(f"🏆 Vitórias : {contador.vitorias}")
        print(f"💀 Derrotas : {contador.derrotas}")

        total = contador.vitorias + contador.derrotas

        if total > 0:
            winrate = (contador.vitorias / total) * 100
            print(f"📈 Win Rate: {winrate:.1f}%")

        print("=" * 25)

    # Fecha com ESC
    if keyboard.is_pressed("esc"):
        contador.parar()
        print("\nPrograma encerrado.")
        break

    time.sleep(0.1)