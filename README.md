# Wordle Simplificado em Python

Este é um projeto educativo inspirado no popular jogo de palavras **Wordle**, desenvolvido em Python. O objetivo é adivinhar uma palavra de 5 letras em até 6 tentativas, com feedback visual a cada jogada.

---

## 📌 Funcionalidades

* Seleção aleatória de uma palavra de 5 letras a partir de uma lista fornecida.
* Validação de entradas do jogador.
* Feedback visual com cores ANSI:

  * 🟩 Verde: letra correta e na posição certa
  * 🟨 Amarelo: letra existe, mas está noutra posição
  * ⬛ Cinzento: letra não existe na palavra
* Pontuação e número de tentativas registados por jogador.
* Exportação dos resultados para um ficheiro Excel.
* Opção de jogar múltiplas partidas.

---

## 🧑‍💻 Tecnologias utilizadas

* Python 3.10+
* Biblioteca `pandas` (para exportar os resultados)
* Biblioteca `openpyxl` (motor para escrita em Excel)

---

## 📁 Estrutura do Projeto

```
wordle_game/
├── game.py           # Código principal do jogo
├── words.txt         # Lista de palavras de 5 letras (uma por linha)
├── requirements.txt  # Lista de dependências do projeto
├── wordle_scores.xlsx # (gerado após exportação de pontuações)
└── README.md         # Documentação do projeto
```

---

## 🚀 Como executar

1. **Clonar o projeto** (ou copiar os ficheiros para uma pasta local).
2. Certificar-se de que o ficheiro `words.txt` está presente com palavras válidas.
3. Criar um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

4. **Instalar as dependências**:

```bash
pip install -r requirements.txt
```

5. **Executar o jogo**:

```bash
python game.py
```

---

## 📜 Formato do ficheiro `words.txt`

O ficheiro `words.txt` deve conter palavras válidas de 5 letras, uma por linha. Exemplo:

```
amigo
livro
tigre
praia
banho
```

---

## 📄 Exportação de Resultados

Durante o jogo, os resultados são armazenados numa lista. O utilizador pode escolher a opção **"Exportar pontuações para Excel"**, que gera o ficheiro `wordle_scores.xlsx` com os seguintes campos:

* Jogador
* Game
* Alvo (palavra alvo)
* Vencedor (se venceu ou não)
* Tentativa (número de tentativas)

---

## 👩‍🏫 Autores

Projeto desenvolvido por:

* Maria Gabriella Rezende
* Guilherme Carmo
* Thales Pires

---

## 🎓 Finalidade Educativa

Este projeto foi desenvolvido como exercício académico para a disciplina de Introdução a Programação, com o objetivo de praticar conceitos como:

* Manipulação de strings e listas
* Estruturas condicionais e loops
* Funções e modularização de código
* Leitura e escrita de ficheiros
* Feedback visual com ANSI
* Exportação de dados para Excel com pandas

---

## 🧠 Melhorias Futuras

* Modo escuro no terminal
* Interface gráfica (Tkinter ou PyGame)
* Dificuldades (fácil, médio, difícil)
* Histórico de jogos por jogador

---

## ✅ Licença

Este projeto é apenas para fins educativos. Livre para uso e adaptação com fins não-comerciais.
