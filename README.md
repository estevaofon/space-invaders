
## 🚀 **Space Invaders - Terminal Edition**

Este é um remake do clássico **Space Invaders**, desenvolvido com **Python** e **curses** para rodar diretamente no terminal. A nave controlada pelo jogador deve destruir os invasores alienígenas antes que eles cheguem à parte inferior da tela. Desafie-se para marcar a maior pontuação possível!

---

### 🛠 **Como Executar**

1. **Pré-requisitos:**
   - **Python 3.x** instalado no sistema.
   - A biblioteca `curses` já está incluída no Python para sistemas Unix (Linux/Mac). Em **Windows**, pode ser necessário instalar **windows-curses**:
     ```bash
     pip install windows-curses
     ```

2. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/space-invaders-terminal.git
   cd space-invaders-terminal
   ```

3. **Executar o jogo:**
   ```bash
   python space_invaders.py
   ```

---

### 🎮 **Como Jogar**

- **Seta Esquerda (←):** Move a nave para a esquerda.
- **Seta Direita (→):** Move a nave para a direita.
- **Espaço:** Atira um projétil.
  
**Objetivo:**  
Destrua o máximo de alienígenas que conseguir antes que eles alcancem a parte inferior da tela!

---

### 📦 **Arquivos**

- **`space_invaders.py`**: Código principal do jogo.
- **`README.md`**: Informações sobre o projeto (este arquivo).

---

### 🌌 **Recursos e Mecânicas**

- **Nave do Jogador:**  
  Representada por uma nave em **ASCII art** e desenhada em **verde**.

  ```
    ▄      
  █████
  ```

- **Invasores Alienígenas:**  
  Representados por uma figura maior, em **magenta**.

  ```
    ▄     ▄  
    ▄█▄▄▄█▄  
  ▄██▄███▄██▄
  █ ▀▄▄ ▄▄▀ █
  ```

- **Explosão Dinâmica:**  
  Cada vez que um alienígena é destruído, uma **explosão animada** acontece na tela, utilizando frames sequenciais e cor amarela:

  ```
   * 
  *****
   * 
  ```

---

### 🚧 **Próximas Melhorias (Ideias)**

- Adicionar níveis com aumento progressivo de dificuldade.
- Incluir vidas ou um sistema de health points (HP) para o jogador.
- Incluir sons com bibliotecas como `pygame` para maior imersão.
- Melhorar a interface para exibir a maior pontuação e nível atual.

---

### 👾 **Contribuição**

Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões e melhorias!

---

### 📜 **Licença**

Este projeto é distribuído sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

### ❤️ **Créditos**

Desenvolvido com Python e a biblioteca `curses`. Inspirado no clássico Space Invaders.
