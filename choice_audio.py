import pygame as pg
import random

pg.mixer.init()

audios_derrota = [
    r"D:\Estudos\PYTHON\Magic Win-Loss Counter\audios\derrotas\smzinho_derrota1.mp3",
    r"D:\Estudos\PYTHON\Magic Win-Loss Counter\audios\derrotas\smzinho_derrota2.mp3",
    r"D:\Estudos\PYTHON\Magic Win-Loss Counter\audios\derrotas\smzinho_derrota3.mp3",
    r"D:\Estudos\PYTHON\Magic Win-Loss Counter\audios\derrotas\smzinho_derrota4.mp3",
    r"D:\Estudos\PYTHON\Magic Win-Loss Counter\audios\derrotas\smzinho_derrota5.mp3",
]

def tocar_derrota():
    audio = random.choice(audios_derrota)
    som = pg.mixer.Sound(audio)
    som.set_volume(0.3)
    som.play()
