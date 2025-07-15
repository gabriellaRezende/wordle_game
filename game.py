# -*- coding: utf-8 -*-
"""
Wordle Simplificado em Python
Versão: 1.0
Autor: Maria Rezende, Guilherme Carmo e Thales Pires
Descrição: Jogo de adivinhação de palavras de 5 letras inspirado no Wordle.
"""

import random
import pandas as pd
import os

# Carrega lista de palavras de 5 letras
# Substitua 'word.txt' pelo ficheiro fornecido pelo docente contendo uma palavra por linha.
WORD_LIST_FILE = 'words.txt'

def load_word_list(filepath):
    """
    Lê o ficheiro de palavras e retorna uma lista de strings.
    Garante que apenas palavras com exatamente 5 letras sejam carregadas.
    """
    palavra = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().lower()
            if len(word) == 5:
                palavra.append(word)
    return palavra

# Função para obter feedback colorido (Thales Pires)
def feedback(palpite, alvo):
    """
    Recebe o palpite e a palavra alvo, devolve uma string com cores ANSI:
    - Verde  : letra correta na posição certa
    - Amarelo: letra existe na palavra mas em posição diferente
    - Cinzento: letra não existe na palavra
    """
    result = []
    alvo_chars = list(alvo)

    # Primeiro passe: marca verdes
    for i, ch in enumerate(palpite):
        if ch == alvo_chars[i]:
            result.append(('green', ch))
            alvo_chars[i] = None  # Consome esta letra
        else:
            result.append((None, ch))

    # Segundo passe: marca amarelos e cinzentos
    for i, (color, ch) in enumerate(result):
        if color is None:
            if ch in alvo_chars:
                result[i] = ('yellow', ch)
                alvo_chars[alvo_chars.index(ch)] = None
            else:
                result[i] = ('grey', ch)
    
    # Constrói string com códigos ANSI
    s = ''
    for color, ch in result:
        if color == 'green':
            s += f"\033[1;32m{ch.upper()}\033[0m"  # Verde
        elif color == 'yellow':
            s += f"\033[1;33m{ch.upper()}\033[0m"  # Amarelo
        else:
            s += f"\033[1;37m{ch.upper()}\033[0m"  # Cinzento
    return s

# Função principal de jogo (guilherme carmo)
def play_wordle(palavra, game_num, scores):
    """
    Executa uma partida de Wordle.
    Retorna True se o jogador ganhou, False caso contrário, e o número de tentativas.
    """
    alvo = random.choice(palavra)
    tentativa = 0
    venceu = False

    print(f"\n=== Jogo #{game_num} ===")
    # Uncomment para debug:
    # print(f"[DEBUG] Palavra alvo: {alvo}")

    while tentativa < 6:
        palpite = input(f"Tentativa {tentativa+1}/6: ").strip().lower()
        # Validação de entrada
        if len(palpite) != 5:
            print("Por favor, insira uma palavra de 5 letras.")
            continue
        if palpite not in palavra:
            print("Palavra não encontrada na lista. Tente outra.")
            continue

        tentativa += 1
        print(feedback(palpite, alvo))

        if palpite == alvo:
            venceu = True
            print(f"Parabéns, {player}! A palavra era '{alvo.upper()}' e você acertou em {tentativa} tentativas.")
            break

    if not venceu:
        print(f"Fim de jogo {player}! Suas tentativas acabaram. A palavra era '{alvo.upper()}'.")

    # Registra resultado
    scores.append({
        'Player': player,
        'Game': game_num,
        'alvo': alvo,
        'venceu': venceu,
        'tentativa': tentativa if venceu else None
    })
    return venceu, tentativa

# Exporta placar para Excel (gabriella rezende)
def export_to_excel(scores, filename='wordle_scores.xlsx'):
    """
    Exporta a lista de dicionários scores para um ficheiro Excel.
    Cada linha terá: Player, Game, alvo, venceu, tentativa.
    """
    df = pd.DataFrame(scores)
    try:
        df.to_excel(filename, index=False)
        print(f"Pontuações exportadas para '{filename}'.")
    except ModuleNotFoundError:
        print("Erro: Pandas não está instalado. Instale com 'pip install pandas openpyxl' para exportar para Excel.")

# Função menu principal (gabriella rezende)
def main():
    # Carrega palavras
    if not os.path.exists(WORD_LIST_FILE):
        print(f"Ficheiro '{WORD_LIST_FILE}' não encontrado. Certifique-se de que exista na mesma pasta.")
        return

    palavra = load_word_list(WORD_LIST_FILE)
    scores = []  # Lista para registar resultados
    game_num = 1

    player = input("Bem-vindo ao Wordle Simplificado! Qual é o seu nome? ").strip()
    if not player:
        player = "Anónimo"

    while True:
        print("\n--- Wordle Simplificado ---")
        print("Regras: Adivinhe a palavra de 5 letras em até 6 tentativas.")
        print("Cores:")
        print("  Verde: letra correta na posição certa")
        print("  Amarelo: letra existe na palavra mas em posição diferente")
        print("  Cinzento: letra não existe na palavra")
        print("----------------" )
        print("1. Jogar uma partida")
        print("2. Exportar pontuações para Excel")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            play_wordle(palavra, game_num, scores)
            game_num += 1
        elif choice == '2':
            export_to_excel(scores)
        elif choice == '3':
            print("Obrigado por jogar! Até à próxima.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
