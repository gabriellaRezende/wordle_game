# -*- coding: utf-8 -*-
"""
Wordle Simplificado em Python
Versão: 1.0
Autor: Maria Rezende, Guilherme Carmo e Thales Pires
Descrição: Jogo de adivinhação de palavras de 5 letras inspirado no Wordle.

Projeto feito em conjunto entre os integrantes do grupo. Ambos tiveram a mesma força de trabalho e desempenho para a conclusão do trabalho.
"""

import random # Importa módulo para gerar palavras aleatórias
import pandas as pd # Importa pandas para manipulação de dados e exportação para Excel
import os # Importa módulo os para manipulação de ficheiros e diretórios

# Define o nome do arquivo com a lista de palavras
WORD_LIST_FILE = 'words.txt'

def load_word_list(filepath):
    """
    Lê o ficheiro de palavras e retorna uma lista de strings.
    Garante que apenas palavras com exatamente 5 letras sejam carregadas.
    """
    palavra = [] #Lista que armazena as palavras validas
    with open(filepath, 'r', encoding='utf-8') as f: # Abre o ficheiro de palavras com UTF-8
        for line in f: # Lê cada linha do ficheiro
            word = line.strip().lower() # Remove espaços e converte para minúsculas
            if len(word) == 5: # Verifica se a palavra tem exatamente 5 letras
                palavra.append(word) # Adiciona a palavra à lista
    return palavra 

# Função para obter feedback colorido
def feedback(palpite, alvo):
    """
    Recebe o palpite e a palavra alvo, devolve uma string com cores ANSI:
    - Verde  : letra correta na posição certa
    - Amarelo: letra existe na palavra mas em posição diferente
    - Cinzento: letra não existe na palavra
    """
    result = [] # Armazena pares (cor, letra)
    alvo_chars = list(alvo) # Converte a palavra alvo em lista de caracteres

    # Primeiro passo: verifica as letras corretas nas posições corretas
    for i, ch in enumerate(palpite): 
        if ch == alvo_chars[i]: #Letra e posição corretas
            result.append(('green', ch)) #Marca Verde
            alvo_chars[i] = None  # Marca como usada
        else:
            result.append((None, ch))  #Ainda não avaliada

    # Segundo passo: verifica as letras corretas mas em posições diferentes ou ausentes
    for i, (color, ch) in enumerate(result):
        if color is None: # Apenas verifica letras ainda não avaliadas
            if ch in alvo_chars:  # Se a letra existe na palavra alvo
                result[i] = ('yellow', ch)  # Marca Amarelo
                alvo_chars[alvo_chars.index(ch)] = None  # Marca como usada
            else:
                result[i] = ('grey', ch) # Marca Cinzento (não existe na palavra)
    
    # Constrói string com códigos ANSI para o terminal
    s = ''
    for color, ch in result:
        if color == 'green':
            s += f"\033[1;32m{ch.upper()}\033[0m"  # Verde
        elif color == 'yellow':
            s += f"\033[1;33m{ch.upper()}\033[0m"  # Amarelo
        else:
            s += f"\033[1;37m{ch.upper()}\033[0m"  # Cinzento
    return s

# Função principal de jogo
def play_wordle(player, palavra, game_num, scores):
    """
    Executa uma partida de Wordle.
    Retorna True se o jogador ganhou, False caso contrário, e o número de tentativas.
    """
    alvo = random.choice(palavra) # Escolhe uma palavra aleatória da lista
    tentativa = 0 # Contador de tentativas
    venceu = False # Flag para verificar se o jogador venceu

    print(f"\n=== Jogo #{game_num} ===") 
    # Uncomment para debug:
    # print(f"[DEBUG] Palavra alvo: {alvo}") # Debug: mostra a palavra alvo 

    while tentativa < 6: # Limite de 6 tentativas
        palpite = input(f"Tentativa {tentativa+1}/6: ").strip().lower() # Lê o palpite do jogador
        # Validação de entrada
        if len(palpite) != 5: # Verifica se o palpite tem 5 letras
            print("Por favor, insira uma palavra de 5 letras.")
            continue
        if palpite not in palavra: # Verifica se a palavra está na lista
            print("Palavra não encontrada na lista. Tente outra.")
            continue

        tentativa += 1 # Incrementa o contador de tentativas
        print(feedback(palpite, alvo)) # Mostra feedback colorido do palpite

        if palpite == alvo: # Verifica se o palpite está correto
            venceu = True # Jogador venceu
            print(f"Parabéns, {player}! A palavra era '{alvo.upper()}' e você acertou em {tentativa} tentativas.")
            break #Fim do jogo se venceu

    if not venceu: # Se não venceu após 6 tentativas
        # Mostra mensagem de fim de jogo
        print(f"Fim de jogo {player}! Suas tentativas acabaram. A palavra era '{alvo.upper()}'.") 

    # Registra resultado da partida
    scores.append({ 
        'Player': player,
        'Game': game_num,
        'alvo': alvo,
        'venceu': venceu,
        'tentativa': tentativa if venceu else None
    })
    return venceu, tentativa 
 
# Exporta placar para Excel
def export_to_excel(scores, filename='wordle_scores.xlsx'):
    """
    Exporta a lista de dicionários scores para um ficheiro Excel.
    Cada linha terá: Player, Game, alvo, venceu, tentativa.
    """
    df = pd.DataFrame(scores) # Converte a lista de dicionários em DataFrame do pandas
    try:
        df.to_excel(filename, index=False) # Exporta para Excel sem índice
        print(f"Pontuações exportadas para '{filename}'.") 
    except ModuleNotFoundError:
        print("Erro: Pandas não está instalado. Instale com 'pip install pandas openpyxl' para exportar para Excel.")

# Função menu principal
def main(): 
    """
    Função principal que inicia o jogo e gerencia o menu.
    Carrega a lista de palavras e inicia o loop do jogo.
    Permite jogar várias partidas e exportar resultados para Excel.
    Se o ficheiro de palavras não existir, informa o usuário.
    """
    # Carrega palavras  
    if not os.path.exists(WORD_LIST_FILE):
        print(f"Ficheiro '{WORD_LIST_FILE}' não encontrado. Certifique-se de que exista na mesma pasta.")
        return

    palavra = load_word_list(WORD_LIST_FILE) # Lista de palavras carregadas
    scores = []  # Lista para registar resultados
    game_num = 1 # Contador de jogos

    # Solicita o nome do jogador    
    player = input("Bem-vindo ao Wordle Simplificado! Qual é o seu nome? ").strip()
    if not player:
        player = "Anónimo" # Nome padrão se o usuário não digitar nada

    # Início do loop principal do jogo
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
            play_wordle(player, palavra, game_num, scores) # Inicia uma nova partida
            game_num += 1 # Incrementa o número do jogo
        elif choice == '2': 
            export_to_excel(scores) # Exporta pontuações para Excel
        elif choice == '3': 
            print("Obrigado por jogar! Até à próxima.") 
            break   
        else:
            print("Opção inválida. Tente novamente.")

#Chama a função principal se o script for executado diretamente
if __name__ == '__main__':
    main()
