import pyautogui as pt
import choice_audio
import time

class WinLossCounter:
    def __init__(self, img_vitoria, img_derrota):
        self.img_vitoria = img_vitoria
        self.img_derrota = img_derrota
        
        self.vitorias = 0
        self.derrotas = 0
        
        self.rodando = False
        self.foi_vencedor = False
        self.foi_derrotado = False

    def iniciar(self):
        self.rodando = True
        while self.rodando:
            self.verificar()
            time.sleep(0.5)

    def parar(self):
        self.rodando = False

    def verificar(self):
        try:
            encontrou_vitoria = pt.locateOnScreen(self.img_vitoria, confidence=0.8)
        except:
            encontrou_vitoria = None

        try:
            encontrou_derrota = pt.locateOnScreen(self.img_derrota, confidence=0.8)
        except:
            encontrou_derrota = None

        # Vitória
        if encontrou_vitoria:
            if not self.foi_vencedor:
                self.vitorias += 1
                self.foi_vencedor = True
        else:
            self.foi_vencedor = False

        # Derrota
        if encontrou_derrota:
            if not self.foi_derrotado:
                self.derrotas += 1
                self.foi_derrotado = True
                choice_audio.tocar_derrota()
        else:
            self.foi_derrotado = False