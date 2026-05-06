import customtkinter as ctk
import threading
from win_loss_counter import WinLossCounter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

counter = None
thread = None

# ----------------------------

def iniciar_jogo(jogo):
    global counter, thread
    
    if counter:
        counter.parar()

    if jogo == "fortnite":
        counter = WinLossCounter(
            "images/imagem_vitoria_fortnite.png",
            "images/imagem_derrota_fortnite.png"
        )

    elif jogo == "magic":
        counter = WinLossCounter(
            "images/imagem_vitoria_magic.png",
            "images/imagem_derrota_magic.png"
        )

    elif jogo == "lol":
        counter = WinLossCounter(
            "images/imagem_vitoria_lol.png",
            "images/imagem_derrota_lol.png"
        )

    thread = threading.Thread(target=counter.iniciar)
    thread.daemon = True
    thread.start()

# ----------------------------

def parar():
    global counter
    if counter:
        counter.parar()

# ----------------------------

def atualizar_label():
    if counter:
        label.configure(text=f"Vitórias: {counter.vitorias} | Derrotas: {counter.derrotas}")
    else:
        label.configure(text="Nenhum jogo iniciado")

    app.after(500, atualizar_label)

# ----------------------------

app = ctk.CTk()
app.title("ScoreMage")
app.geometry("350x250")
app.resizable(False, False)

titulo = ctk.CTkLabel(app, text="Escolha o jogo", font=("Arial", 18))
titulo.pack(pady=10)

btn_magic = ctk.CTkButton(app, text="Magic", command=lambda: iniciar_jogo("magic"))
btn_magic.pack(pady=5)

btn_fortnite = ctk.CTkButton(app, text="Fortnite", command=lambda: iniciar_jogo("fortnite"))
btn_fortnite.pack(pady=5)

btn_lol = ctk.CTkButton(app, text="League of Legends", command=lambda: iniciar_jogo("lol"))
btn_lol.pack(pady=5)

btn_parar = ctk.CTkButton(app, text="Parar", fg_color="red", command=parar)
btn_parar.pack(pady=10)

label = ctk.CTkLabel(app, text="Nenhum jogo iniciado")
label.pack(pady=10)

atualizar_label()

app.mainloop()