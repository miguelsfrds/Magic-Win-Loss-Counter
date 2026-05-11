import pygame as pg
import random
import os
import sys

# Pasta onde o executável (ou o script) está localizado
if getattr(sys, 'frozen', False):
    # Rodando como .exe gerado pelo PyInstaller
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # Rodando como script Python normal
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def caminho_audio(nome_arquivo):
    return os.path.join(BASE_DIR, "audios", "derrotas", nome_arquivo)

audios_derrota = [
    caminho_audio("smzinho_derrota1.mp3"),
    caminho_audio("smzinho_derrota2.mp3"),
    caminho_audio("smzinho_derrota3.mp3"),
    caminho_audio("smzinho_derrota4.mp3"),
    caminho_audio("smzinho_derrota5.mp3"),
]

# Inicializa o pygame.mixer apenas uma vez, com verificação de erro
def inicializar_audio():
    try:
        if not pg.mixer.get_init():
            pg.mixer.init()
            print("[Audio] pygame.mixer inicializado com sucesso.")
    except Exception as e:
        print(f"[Audio] ERRO ao inicializar pygame.mixer: {e}")

def tocar_derrota():
    try:
        inicializar_audio()

        audios_validos = [a for a in audios_derrota if os.path.exists(a)]

        if not audios_validos:
            print("[Audio] AVISO: Nenhum arquivo de áudio encontrado. Verifique os caminhos:")
            for a in audios_derrota:
                print(f"  - {a}")
            return

        audio = random.choice(audios_validos)
        som = pg.mixer.Sound(audio)
        som.set_volume(0.3)
        som.play()
        print(f"[Audio] Tocando: {audio}")

    except Exception as e:
        print(f"[Audio] ERRO ao tocar áudio: {e}")