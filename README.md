<p align="center">
  <img src="https://github.com/user-attachments/assets/3b923f1a-d560-46d6-ad1d-725950d51418" width=800px/>
</p>

> Contador automático de vitórias e derrotas para jogos online — sem digitar nada, só jogar.

---

## 🎮 O que é o Project Tallyo?

O **Project Tallyo** é uma ferramenta de terminal que monitora sua tela em tempo real e detecta automaticamente quando você venceu ou perdeu uma partida. Chega de ficar anotando no papel ou perdendo a conta no meio de uma sessão intensa — o Tallyo faz isso por você.

E quando você toma uma derrota... ele ainda te trolleia com um áudio surpresa. 😈

---

## ✨ Funcionalidades

- 👁️ **Detecção automática por visão computacional** — reconhece telas de vitória e derrota usando reconhecimento de imagem
- 📊 **Placar em tempo real** — vitórias, derrotas e winrate atualizados ao vivo no terminal
- 🔊 **Reação sonora nas derrotas** — toca um áudio aleatório ao detectar uma derrota
- 🎮 **Suporte a múltiplos jogos** — escolha o jogo pelo número no menu
- 🧵 **Monitoramento em thread separada** — o tracker roda em background sem travar o terminal
- 🛑 **Encerramento com ESC** — pressione ESC a qualquer momento para parar
- 🖥️ **Compatível com Windows com escala de tela** — funciona corretamente em monitores com DPI 125%, 150% etc.

---

## 🕹️ Jogos Suportados

| Jogo | Status |
|---|---|
| 🪄 Magic: The Gathering | ✅ Integrado |
| 💥 Fortnite | ✅ Integrado |

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
| `pyautogui` | Captura de tela e reconhecimento de imagem |
| `pygame` | Reprodução dos áudios de derrota |
| `keyboard` | Detecção do ESC para encerrar o programa |
| `threading` | Monitoramento em background sem travar o terminal |
| `ctypes` | Correção de DPI para monitores com escala no Windows |

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
pip install pyautogui pygame keyboard
```

### Execução

```bash
python main.py
```

---

## 📦 Gerando o Executável (.exe)

Para distribuir o programa sem precisar do Python instalado:

```bash
# Instale o PyInstaller
pip install pyinstaller

# Gere o executável (as imagens são embutidas; os áudios ficam externos)
pyinstaller --onefile --icon=icone.ico --add-data "images;images" main.py
```

O executável será gerado em `dist/main.exe`.

### ⚠️ Importante: copiar a pasta de áudios

Os áudios **não são embutidos** no executável — eles ficam em uma pasta ao lado do `.exe`. Após gerar, copie a pasta `audios` para dentro de `dist/`:

```bash
xcopy audios dist\audios /E /I
```

A estrutura final em `dist/` deve ser:

```
dist/
├── main.exe
└── audios/
    └── derrotas/
        ├── smzinho_derrota1.mp3
        ├── smzinho_derrota2.mp3
        └── ...
```

> O programa sempre busca os áudios na pasta `audios/derrotas/` relativa ao local do executável, então ele funciona em qualquer diretório desde que a pasta esteja ao lado do `.exe`.

---

## 📁 Estrutura do Projeto

```
project-tallyo/
│
├── main.py               # Ponto de entrada: menu, loop principal e placar no terminal
├── win_loss_counter.py   # Lógica de detecção e contagem
├── choice_audio.py       # Seleção e reprodução de áudios de derrota
├── choice_game.py        # Registro dos jogos e caminhos das imagens
├── icone.ico             # Ícone do executável
├── main.spec             # Configuração do PyInstaller
│
├── images/               # Imagens de referência para detecção
│   ├── imagem_vitoria_magic.png
│   ├── imagem_derrota_magic.png
│   ├── imagem_vitoria_fortnite.png
│   └── imagem_derrota_fortnite.png
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

**2.** Registre o jogo em `choice_game.py`:
```python
"Seu Jogo": {
    "vitoria": caminho_arquivo("images/imagem_vitoria_seujogo.png"),
    "derrota": caminho_arquivo("images/imagem_derrota_seujogo.png")
}
```

Pronto. O menu vai exibir o novo jogo automaticamente na próxima execução.

> 💡 **Dica:** Use imagens de referência com elementos únicos e estáticos da tela de fim de partida para evitar falsos positivos.

---

## 🐛 Diagnóstico de Problemas

O programa exibe mensagens de debug no terminal para facilitar identificação de problemas:

| Mensagem | O que significa |
|---|---|
| `[Debug] ARQUIVO NÃO ENCONTRADO: ...` | O caminho da imagem de referência está errado |
| `[Debug] Vitória detectada!` | Imagem de vitória encontrada na tela |
| `[Debug] Derrota detectada!` | Imagem de derrota encontrada na tela |
| `[Audio] AVISO: Nenhum arquivo de áudio encontrado` | A pasta `audios/derrotas/` não está ao lado do executável |
| `[Audio] Tocando: ...` | Áudio sendo reproduzido com sucesso |

---

## 📌 Melhorias Futuras

- [ ] Histórico de sessões com data e hora
- [ ] Gráfico de desempenho ao longo do tempo
- [ ] Suporte a áudios de vitória
- [ ] Exportar placar para `.csv` ou `.txt`
- [ ] Configuração de confiança de detecção via argumento na linha de comando
- [ ] Interface gráfica opcional

---

## 👨‍💻 Autor

Desenvolvido por **[@miguelsfrds](https://github.com/miguelsfrds)**

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
