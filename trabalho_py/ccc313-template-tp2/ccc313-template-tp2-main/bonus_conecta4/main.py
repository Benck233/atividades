"""
Conecta 4 — Loop principal do jogo
====================================
Fornecido pelo professor. NÃO MODIFIQUE ESTE ARQUIVO.

Execução interativa (stdin em TTY):
    python main.py
    → Informe nome e se cada jogador é CPU nas perguntas iniciais.

Execução via replay (autograder / script):
    echo "J1 J2\n0\n1\n0" | python main.py
    → Formato legado: apenas os nomes na 1a linha (nome "CPU" ativa IA).

    echo "J1 J2 s n\n0\n1\n0" | python main.py
    → Formato explicito: "nome1 nome2 cpu1 cpu2" na 1a linha.
      cpu1/cpu2 aceitam: s/sim/y/yes/1/true/cpu ou n/nao/no/0/false.

    Cada linha seguinte representa a coluna escolhida pelo jogador atual.
"""

import sys
import os

# Garante importação correta independente do diretório de trabalho
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from interface import get_console, render_board, show_result, J1, J2, COLUNAS
from game import (
    criar_tabuleiro,
    validar_jogada,
    fazer_jogada,
    verificar_vitoria,
    tabuleiro_cheio,
    obter_jogada_cpu,
)


def _info(msg: str, interactive: bool) -> None:
    """Imprime mensagens auxiliares apenas no modo interativo."""
    if interactive:
        print(msg)


def _parse_yes_no(ans: str) -> bool | None:
    """Converte respostas de sim/nao em bool; retorna None se inválida."""
    normalizado = ans.strip().lower()
    yes = {"s", "sim", "y", "yes", "1", "true", "cpu"}
    no = {"n", "nao", "não", "no", "0", "false", "humano", "player"}
    if normalizado in yes:
        return True
    if normalizado in no:
        return False
    return None


def _ask_cpu_flag(player_idx: int) -> bool:
    """Pergunta até receber uma resposta válida para CPU (s/n)."""
    while True:
        parsed = _parse_yes_no(input(f"Jogador {player_idx} e CPU? (s/n): "))
        if parsed is not None:
            return parsed
        print("Resposta invalida. Use s/sim ou n/nao.")


def _players_from_non_tty_line(line: str) -> list[dict[str, str | bool]]:
    """Monta jogadores no modo non-TTY a partir da primeira linha."""
    tokens = line.split()
    if len(tokens) < 2:
        print("Erro: informe ao menos dois nomes na primeira linha.")
        sys.exit(1)

    if len(tokens) == 2:
        j1_nome, j2_nome = tokens
        # Compatibilidade com scripts antigos: nome "CPU" ativa IA.
        return [
            {"nome": j1_nome, "peca": J1, "cpu": j1_nome.upper() == "CPU"},
            {"nome": j2_nome, "peca": J2, "cpu": j2_nome.upper() == "CPU"},
        ]

    if len(tokens) == 4:
        j1_nome, j2_nome, j1_cpu_raw, j2_cpu_raw = tokens
        j1_cpu = _parse_yes_no(j1_cpu_raw)
        j2_cpu = _parse_yes_no(j2_cpu_raw)
        if j1_cpu is None or j2_cpu is None:
            print("Erro: cpu1/cpu2 invalidos. Use s/sim/y/yes/1/true ou n/nao/no/0/false.")
            sys.exit(1)
        return [
            {"nome": j1_nome, "peca": J1, "cpu": j1_cpu},
            {"nome": j2_nome, "peca": J2, "cpu": j2_cpu},
        ]

    print("Erro: formato invalido na primeira linha. Use 'J1 J2' ou 'J1 J2 cpu1 cpu2'.")
    sys.exit(1)


def main() -> None:
    console = get_console()

    # ── Leitura dos nomes/configuração ──────────────────────────────────────
    _stdin_is_tty = sys.stdin.isatty()

    if _stdin_is_tty:
        j1_nome = input("Nome do Jogador 1: ").strip()
        j1_cpu = _ask_cpu_flag(1)
        j2_nome = input("Nome do Jogador 2: ").strip()
        j2_cpu = _ask_cpu_flag(2)

        players: list[dict[str, str | bool]] = [
            {"nome": j1_nome, "peca": J1, "cpu": j1_cpu},
            {"nome": j2_nome, "peca": J2, "cpu": j2_cpu},
        ]
    else:
        players = _players_from_non_tty_line(input())

    board = criar_tabuleiro()
    turno = 0
    last_col = None

    while True:
        jogador_info = players[turno % 2]
        jogador_atual = str(jogador_info["nome"])
        peca_atual = str(jogador_info["peca"])
        jogador_cpu = bool(jogador_info["cpu"])

        render_board(board, console, jogador_atual, peca_atual, last_col)

        # ── Leitura ou cálculo da jogada ─────────────────────────────────────
        if jogador_cpu:
            col = obter_jogada_cpu(board, peca_atual)
            _info(f"{jogador_atual} (CPU) escolheu coluna {col}", _stdin_is_tty)
        else:
            try:
                if _stdin_is_tty:
                    entrada_jogada = input(f"Proxima jogada de {jogador_atual} (0-{COLUNAS - 1}): ")
                else:
                    entrada_jogada = input()
                col = int(entrada_jogada)
            except EOFError:
                break
            except ValueError:
                _info("Entrada inválida. Tente novamente.", _stdin_is_tty)
                continue

        # ── Validação ────────────────────────────────────────────────────────
        erro = validar_jogada(board, col)
        if erro is not None:
            _info(erro, _stdin_is_tty)
            continue

        # ── Execução da jogada ───────────────────────────────────────────────
        fazer_jogada(board, col, peca_atual)
        last_col = col

        # ── Verificação de fim de jogo ───────────────────────────────────────
        if verificar_vitoria(board, peca_atual):
            render_board(board, console, jogador_atual, peca_atual, last_col)
            show_result(f"{jogador_atual} venceu!", console)
            break

        if tabuleiro_cheio(board):
            render_board(board, console, jogador_atual, peca_atual, last_col)
            show_result("Empate!", console)
            break

        turno += 1


if __name__ == "__main__":
    main()
