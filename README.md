# 🎯 Project Tallyo

> Contador automático de vitórias e derrotas para jogos online — sem digitar nada, só jogar.

---

## 🎮 O que é o Project Tallyo?

O **Project Tallyo** é uma ferramenta desktop que monitora sua tela em tempo real e detecta automaticamente quando você venceu ou perdeu uma partida. Chega de ficar anotando no papel ou perdendo a conta no meio de uma sessão intensa — o Tallyo faz isso por você.

E quando você toma uma derrota... ele ainda te trolleia com um áudio surpresa. 😈

---

## ✨ Funcionalidades

- 👁️ **Detecção automática por visão computacional** — reconhece telas de vitória e derrota usando reconhecimento de imagem
- 📊 **Placar em tempo real** — vitórias e derrotas atualizados ao vivo na interface
- 🔊 **Reação sonora nas derrotas** — toca um áudio aleatório ao detectar uma derrota
- 🎮 **Suporte a múltiplos jogos** — troca de jogo com um clique, sem reiniciar
- 🧵 **Monitoramento em thread separada** — o tracker roda em background sem travar a interface
- 🛑 **Controle total** — botão dedicado para pausar o monitoramento a qualquer momento

---

## 🕹️ Jogos Suportados

| Jogo | Status |
|---|---|
| 🪄 Magic: The Gathering | ✅ Integrado |
| 💥 Fortnite | ✅ Integrado |
| ⚔️ League of Legends | ✅ Integrado |

> Quer adicionar outro jogo? Veja a seção [Adicionando Novos Jogos](#-adicionando-novos-jogos).

---

## 🧠 Como Funciona

O **Project Tallyo** usa a biblioteca `pyautogui` para capturar screenshots da tela a cada **0,5 segundos** e compara os frames com imagens de referência de vitória/derrota de cada jogo.

```
Loop de monitoramento (a cada 0.5s):
  ├── Captura a tela atual
  ├── Procura a imagem de vitória → se encontrar (confiança ≥ 80%), incrementa vitórias
  └── Procura a imagem de derrota → se encontrar (confiança ≥ 80%), incrementa derrotas + toca áudio
```

A lógica de flag (`foi_vencedor` / `foi_derrotado`) garante que **cada resultado seja contado apenas uma vez**, mesmo que a tela de fim de partida fique visível por vários segundos.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| `Python 3.x` | Linguagem base |
| `customtkinter` | Interface gráfica moderna |
| `pyautogui` | Captura de tela e reconhecimento de imagem |
| `pygame` | Reprodução dos áudios de derrota |
| `threading` | Monitoramento em background sem travar a UI |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- As dependências listadas abaixo

### Instalação

```bash
# Clone o repositório
git clone https://github.com/miguelsfrds/project-tallyo.git
cd project-tallyo

# Instale as dependências
pip install customtkinter pyautogui pygame
```

### Execução

```bash
python interface.py
```

---

## 📁 Estrutura do Projeto

```
project-tallyo/
│
├── interface.py          # Interface gráfica principal
├── win_loss_counter.py   # Lógica de detecção e contagem
├── choice_audio.py       # Seleção e reprodução de áudios
│
├── images/               # Imagens de referência para detecção
│   ├── imagem_vitoria_magic.png
│   ├── imagem_derrota_magic.png
│   ├── imagem_vitoria_fortnite.png
│   ├── imagem_derrota_fortnite.png
│   ├── imagem_vitoria_lol.png
│   └── imagem_derrota_lol.png
│
├── audios/
│   └── derrotas/         # Áudios tocados ao detectar derrota
│       ├── smzinho_derrota1.mp3
│       └── ...
│
└── README.md
```

---

## ➕ Adicionando Novos Jogos

Integrar um novo jogo ao Project Tallyo é simples:

**1.** Tire prints das telas de vitória e derrota do jogo e salve em `images/`:
```
images/imagem_vitoria_seujogo.png
images/imagem_derrota_seujogo.png
```

**2.** Adicione um botão na interface (`interface.py`):
```python
btn_seujogo = ctk.CTkButton(app, text="Seu Jogo", command=lambda: iniciar_jogo("seujogo"))
btn_seujogo.pack(pady=5)
```

**3.** Registre o jogo na função `iniciar_jogo`:
```python
elif jogo == "seujogo":
    counter = WinLossCounter(
        "images/imagem_vitoria_seujogo.png",
        "images/imagem_derrota_seujogo.png"
    )
```

> 💡 **Dica:** Use imagens de referência com elementos únicos e estáticos da tela de fim de partida para evitar falsos positivos.

---

## 📌 Melhorias Futuras

- [ ] Histórico de sessões com data e hora
- [ ] Gráfico de desempenho ao longo do tempo
- [ ] Suporte a áudios de vitória
- [ ] Exportar placar para `.csv` ou `.txt`
- [ ] Configuração de confiança de detecção pela interface
- [ ] Sistema de perfis por jogador

---

## 👨‍💻 Autor

Desenvolvido por **[@miguelsfrds](https://github.com/miguelsfrds)**

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
