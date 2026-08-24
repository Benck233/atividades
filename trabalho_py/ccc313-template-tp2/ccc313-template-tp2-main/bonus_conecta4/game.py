"""
Conecta 4 — Lógica do Jogo
============================

Implemente as 6 funções abaixo. Não modifique as assinaturas nem os arquivos
main.py ou interface.py.

────────────────────────────────────────────────────────────────────────────────
Regras do Conecta 4
────────────────────────────────────────────────────────────────────────────────
• Tabuleiro de 6 linhas × 7 colunas.
• Dois jogadores alternam turnos colocando peças em colunas (0 a 6).
• As peças "caem" por gravidade: ocupam sempre a posição mais baixa livre.
• Vence quem conectar 4 peças consecutivas em qualquer direção:
    – horizontal  (mesma linha),
    – vertical    (mesma coluna),
    – diagonal \\  (linha e coluna crescem juntas),
    – diagonal /  (linha decresce enquanto coluna cresce).
• Se o tabuleiro encher sem vencedor, o jogo termina em empate.

────────────────────────────────────────────────────────────────────────────────
Constantes disponíveis (importadas de interface.py)
────────────────────────────────────────────────────────────────────────────────
  VAZIO   → célula vazia ("."), valor inicial de cada posição
  J1      → peça do jogador 1 ("X")
  J2      → peça do jogador 2 ("O")
  LINHAS  → número de linhas do tabuleiro (6)
  COLUNAS → número de colunas do tabuleiro (7)

────────────────────────────────────────────────────────────────────────────────
Representação do tabuleiro
────────────────────────────────────────────────────────────────────────────────
  board é uma lista de listas: board[linha][coluna]
  board[0]  → topo   (linha 0)
  board[5]  → base   (linha 5, onde as peças caem primeiro)

  Exemplo de acesso: board[2][3] é a célula na linha 2, coluna 3.

────────────────────────────────────────────────────────────────────────────────
[BÔNUS] IA simples
────────────────────────────────────────────────────────────────────────────────
Se um jogador se chamar "CPU", main.py chama obter_jogada_cpu() em vez de ler
do teclado. Implemente essa função para ganhar os pontos de bônus.
O bônus é avaliado manualmente pelo professor — não há teste automático.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from interface import VAZIO, LINHAS, COLUNAS


# ─────────────────────────────────────────────────────────────────────────────
# Parte 1 — Estrutura do tabuleiro
# ─────────────────────────────────────────────────────────────────────────────

def criar_tabuleiro() -> list:
    """
    Retorna um tabuleiro vazio: lista de LINHAS listas, cada uma com COLUNAS
    strings iguais a VAZIO.

    Dica: use uma compreensão de lista aninhada.

    Exemplo de uso:
        board = criar_tabuleiro()
        print(board[0])  # ['.', '.', '.', '.', '.', '.', '.']
    """
    return [[VAZIO] * COLUNAS for _ in range(LINHAS)]


# ─────────────────────────────────────────────────────────────────────────────
# Parte 2 — Validação e execução de jogadas
# ─────────────────────────────────────────────────────────────────────────────

def eh_valido(board: list, col: int) -> bool:
    """
    Retorna True se for possível jogar na coluna col.

    Uma coluna é válida quando:
      1. col está no intervalo [0, COLUNAS - 1], e
      2. a posição do topo dessa coluna (linha 0) ainda está vazia.

    Exemplos:
        eh_valido(board, -1)  → False  (fora do tabuleiro)
        eh_valido(board, 7)   → False  (fora do tabuleiro)
        eh_valido(board, 3)   → True   (coluna 3 com espaço disponível)
    """
    return validar_jogada(board, col) is None


def validar_jogada(board: list, col: int) -> str | None:
    """
    Retorna None se a jogada for valida; caso contrario, retorna uma mensagem
    curta explicando o erro.

    Esta funcao foi separada para facilitar manutencao e leitura no loop do jogo,
    permitindo exibir ao jogador o motivo exato da jogada invalida.
    """
    if not isinstance(col, int):
        return "Entrada invalida: informe um numero inteiro."
    if col < 0 or col >= COLUNAS:
        return f"Coluna invalida: use um valor entre 0 e {COLUNAS - 1}."
    if board[0][col] != VAZIO:
        return f"Coluna {col} cheia. Escolha outra coluna."
    return None


def fazer_jogada(board: list, col: int, peca: str) -> int:
    """
    Insere peca na coluna col na posição mais baixa livre (gravidade).
    Modifica board in-place e retorna o índice da linha onde a peça caiu.

    Esta função assume que a jogada já foi validada com eh_valido().

    Dica: percorra as linhas de baixo para cima com range(LINHAS-1, -1, -1)
          e insira a peça na primeira célula igual a VAZIO.

    Exemplo:
        board = criar_tabuleiro()
        linha = fazer_jogada(board, 3, J1)
        print(linha)         # 5  (caiu na última linha)
        print(board[5][3])   # "X"
    """
    for row in range(LINHAS - 1, -1, -1):
        if board[row][col] == VAZIO:
            board[row][col] = peca
            return row
    return -1


# ─────────────────────────────────────────────────────────────────────────────
# Parte 3 — Verificação de fim de jogo
# ─────────────────────────────────────────────────────────────────────────────

def verificar_vitoria(board: list, peca: str) -> bool:
    """
    Retorna True se peca tiver 4 em linha no tabuleiro atual.

    Verifique as 4 direções:
      • Horizontal:  board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]
      • Vertical:    board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]
      • Diagonal \\: board[r][c], board[r+1][c+1], ...
      • Diagonal /:  board[r][c], board[r-1][c+1], ...  (use r a partir de 3)

    Dica: para cada direção, itere sobre todas as posições iniciais válidas e
          verifique se os 4 elementos consecutivos são todos iguais a peca.
          A função all() com uma compreensão pode simplificar muito o código.
    """
    # Horizontal
    for r in range(LINHAS):
        for c in range(COLUNAS - 3):
            if all(board[r][c + i] == peca for i in range(4)):
                return True
    # Vertical
    for r in range(LINHAS - 3):
        for c in range(COLUNAS):
            if all(board[r + i][c] == peca for i in range(4)):
                return True
    # Diagonal \\
    for r in range(LINHAS - 3):
        for c in range(COLUNAS - 3):
            if all(board[r + i][c + i] == peca for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, LINHAS):
        for c in range(COLUNAS - 3):
            if all(board[r - i][c + i] == peca for i in range(4)):
                return True
    return False


def tabuleiro_cheio(board: list) -> bool:
    """
    Retorna True se o tabuleiro não tiver nenhuma célula vazia.

    Dica: basta verificar a linha 0 (topo) — se nenhuma coluna do topo
          estiver vazia, o tabuleiro inteiro está cheio (pela gravidade).
    """
    return all(board[0][c] != VAZIO for c in range(COLUNAS))


# ─────────────────────────────────────────────────────────────────────────────
# [BÔNUS] IA simples — opcional, sem teste automático
# ─────────────────────────────────────────────────────────────────────────────

def obter_jogada_cpu(board: list, peca: str) -> int:
    """
    Retorna o índice da coluna escolhida pela IA para jogar com peca.

    Heurística sugerida (da mais para a menos prioritária):
      1. Se a CPU pode vencer neste turno, jogue na coluna vencedora.
      2. Se o adversário pode vencer no próximo turno, bloqueie.
      3. Prefira a coluna central (3) e colunas próximas ao centro.
      4. Caso contrário, escolha aleatoriamente entre as colunas válidas.

    Para ativar a IA, informe "CPU" como nome de um dos jogadores:
        python main.py   →  entrada: "Alice CPU"

    O bônus é avaliado manualmente. A implementação abaixo é um fallback
    aleatório — substitua pela sua heurística.
    """
    # TODO (bônus): substitua pelo comportamento inteligente
    import random
    validas = [c for c in range(COLUNAS) if eh_valido(board, c)]
    return random.choice(validas) if validas else -1
