# 🃏 Magic Win/Loss Counter

> Contador automático de vitórias e derrotas para **Magic: The Gathering Arena** usando reconhecimento de imagem em tempo real.

---

## 📖 Sobre o Projeto

O **Magic Win/Loss Counter** é um script Python que monitora sua tela continuamente e detecta automaticamente quando você vence ou perde uma partida no Magic: The Gathering Arena. Ele faz isso comparando o conteúdo da tela com imagens de referência (tela de vitória e tela de derrota), usando visão computacional para identificar o momento exato do resultado.

Chega de anotar resultados manualmente — o bot cuida disso pra você!

---

## ✨ Funcionalidades

- 🔍 **Detecção automática** de vitórias e derrotas por reconhecimento de imagem
- 📊 **Contador em tempo real** exibido no terminal com formatação colorida
- 🛡️ **Anti-duplicata**: cada resultado é contado apenas uma vez por partida
- ⌨️ **Encerramento fácil** — pressione `Q` para parar o script a qualquer momento
- 🎨 **Output estilizado** com a biblioteca `rich` (cores, formatação, ícones)

---

## 🗂️ Estrutura do Projeto

```
magic-counter/
│
├── main.py                        # Script principal
├── imagem_derrota_magic.png       # Imagem de referência para derrota
├── imagem_vitoria_magic.png       # Imagem de referência para vitória
└── README.md
```

---

## 🛠️ Requisitos

- Python **3.8+**
- Sistema operacional: **Windows** (recomendado para uso com `pyautogui` e `keyboard`)

### Dependências

Instale todas com:

```bash
pip install pyautogui keyboard rich
```

| Biblioteca    | Uso                                               |
|---------------|---------------------------------------------------|
| `pyautogui`   | Captura de tela e localização de imagens          |
| `keyboard`    | Detecção do atalho de teclado para encerrar       |
| `rich`        | Formatação colorida e estilizada no terminal      |

> ⚠️ **Nota:** Em sistemas Linux/macOS, pode ser necessário instalar dependências adicionais para o `pyautogui` funcionar corretamente (como `scrot`, `python3-xlib`).

---

## 🚀 Como Usar

### 1. Prepare as imagens de referência

Tire prints das telas de **vitória** e **derrota** do Magic Arena e salve como:

- `imagem_vitoria_magic.png`
- `imagem_derrota_magic.png`

> 💡 **Dica:** Quanto mais específica e única for a região capturada (ex: só o banner "Victory!" ou "Defeat"), melhor será a precisão da detecção.

### 2. Execute o script

```bash
python main.py
```

### 3. Jogue normalmente!

O script roda em segundo plano monitorando a tela. Os resultados aparecem automaticamente no terminal:

```
[+] Vitória detectada! Total de vitórias: 1
[+] Derrota detectada! Total de derrotas: 1
```

### 4. Para encerrar

Pressione **`Q`** a qualquer momento.

---

## ⚙️ Como Funciona

```
┌─────────────────────────────────────────────────┐
│              Loop principal (0.5s)              │
│                                                 │
│  1. Captura a tela atual                        │
│  2. Compara com imagem_vitoria_magic.png        │
│     → Se match (conf. ≥ 0.8): conta vitória    │
│  3. Compara com imagem_derrota_magic.png        │
│     → Se match (conf. ≥ 0.8): conta derrota    │
│  4. Exibe resultado no terminal                 │
│  5. Pressione Q para encerrar                   │
└─────────────────────────────────────────────────┘
```

A **confiança mínima de 0.8 (80%)** evita falsos positivos — o script só conta o resultado quando tem certeza do que viu na tela.

As flags `foi_derrotado` e `foi_vencedor` garantem que um mesmo resultado não seja contado mais de uma vez enquanto a tela de resultado ainda estiver visível.

---

## 🎛️ Configurações

No topo do arquivo `main.py` você pode ajustar:

```python
imagem_derrota = "imagem_derrota_magic.png"   # Caminho da imagem de derrota
imagem_vitoria = "imagem_vitoria_magic.png"   # Caminho da imagem de vitória
```

E dentro da função `locateOnScreen`, o parâmetro `confidence`:

```python
pt.locateOnScreen(imagem_vitoria, confidence=0.8)
#                                             ^^^
#                     Ajuste entre 0.0 e 1.0 conforme necessário
```

- **Aumentar** a confiança → menos falsos positivos, mas pode deixar de detectar
- **Diminuir** a confiança → mais sensível, mas pode contar resultados incorretos

---

## 🐛 Problemas Comuns

| Problema | Possível Causa | Solução |
|---|---|---|
| Não detecta nada | Imagens de referência diferentes da resolução atual | Recapture as imagens na mesma resolução do jogo |
| Conta a mesma partida duas vezes | Confiança muito baixa | Aumente o valor de `confidence` |
| Erro ao importar `keyboard` | Falta de permissão de administrador | Execute o terminal como **administrador** |
| Script trava ao pressionar Q | Conflito com o foco do jogo | Alt+Tab para o terminal e pressione Q |

---

## 📈 Possíveis Melhorias Futuras

- [ ] Interface gráfica (GUI) com placar visual
- [ ] Salvar histórico de partidas em arquivo `.csv` ou banco de dados
- [ ] Calcular winrate automático
- [ ] Suporte a múltiplos jogos/perfis
- [ ] Notificações sonoras ao detectar resultado

---

## 📄 Licença

Este projeto é de uso livre para fins pessoais. Sinta-se à vontade para modificar e melhorar!

---

<div align="center">
  Feito com ☕ e muito <strong>Magic</strong> 🃏
</div>
