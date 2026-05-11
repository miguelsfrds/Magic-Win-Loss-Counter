import pyautogui as pt
import threading
import time
import choice_audio

# CORREÇÃO CRÍTICA: desativa o failsafe do pyautogui (mover mouse pro canto não mata o programa)
pt.FAILSAFE = False

# CORREÇÃO DE DPI: faz o pyautogui capturar na resolução real do Windows
# Necessário quando a escala do Windows está em 125%, 150%, etc.
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # PROCESS_PER_MONITOR_DPI_AWARE
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


class WinLossCounter:
    def __init__(self, img_vitoria, img_derrota):
        self.img_vitoria = img_vitoria
        self.img_derrota = img_derrota

        self.vitorias = 0
        self.derrotas = 0

        self.rodando = False
        self.foi_vencedor = False
        self.foi_derrotado = False

        # Fila de áudios para tocar na thread principal
        self._tocar_audio = False

    def iniciar(self):
        self.rodando = True
        while self.rodando:
            self.verificar()
            time.sleep(0.5)

    def parar(self):
        self.rodando = False

    def verificar(self):
        # Tenta encontrar vitória
        encontrou_vitoria = self._encontrar_imagem(self.img_vitoria, label="vitória")

        # Tenta encontrar derrota
        encontrou_derrota = self._encontrar_imagem(self.img_derrota, label="derrota")

        # Vitória
        if encontrou_vitoria:
            if not self.foi_vencedor:
                self.vitorias += 1
                self.foi_vencedor = True
                print("[Debug] Vitória detectada!")
        else:
            self.foi_vencedor = False

        # Derrota
        if encontrou_derrota:
            if not self.foi_derrotado:
                self.derrotas += 1
                self.foi_derrotado = True
                print("[Debug] Derrota detectada!")
                # Toca áudio em thread separada para não travar o loop
                threading.Thread(target=choice_audio.tocar_derrota, daemon=True).start()
        else:
            self.foi_derrotado = False

    def _encontrar_imagem(self, caminho, label="imagem"):
        """Tenta localizar uma imagem na tela com diagnóstico de erro."""
        import os

        if not os.path.exists(caminho):
            print(f"[Debug] ARQUIVO NÃO ENCONTRADO: {caminho}")
            return None

        try:
            resultado = pt.locateOnScreen(caminho, confidence=0.8)
            return resultado
        except pt.ImageNotFoundException:
            # Imagem não está na tela — comportamento normal
            return None
        except Exception as e:
            print(f"[Debug] Erro ao buscar {label} ({caminho}): {e}")
            return None