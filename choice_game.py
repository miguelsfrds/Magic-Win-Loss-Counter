import os
import sys

def caminho_arquivo(rel_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, rel_path)


jogos = {

    "Magic": {

        "vitoria": caminho_arquivo(
            "images/imagem_vitoria_magic.png"
        ),

        "derrota": caminho_arquivo(
            "images/imagem_derrota_magic.png"
        )
    },

    "Fortnite": {

        "vitoria": caminho_arquivo(
            "images/imagem_vitoria_fortnite.png"
        ),

        "derrota": caminho_arquivo(
            "images/imagem_derrota_fortnite.png"
        )
    }
}