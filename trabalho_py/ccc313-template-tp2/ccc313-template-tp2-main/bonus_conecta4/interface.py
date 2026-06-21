"""
Interface do Conecta 4 — funções fornecidas pelo professor
==========================================================
Fornecido pelo professor. NÃO MODIFIQUE ESTE ARQUIVO.

Este módulo cuida exclusivamente da exibição do tabuleiro e das mensagens
de resultado. Em modo interativo (TTY) utiliza a biblioteca rich para uma
apresentação colorida; em modo não-interativo (stdin redirecionado, como
ocorre no autograder) exibe ASCII simples para garantir comparação exata
de saída.
"""

import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich import box

# ── Constantes do jogo ───────────────────────────────────────────────────────
VAZIO = "."
J1 = "X"
J2 = "O"
LINHAS = 6
COLUNAS = 7

_IS_TTY: bool = sys.stdout.isatty()
_ENCODING = (sys.stdout.encoding or "").lower()
_SUPPORTS_UNICODE: bool = any(enc in _ENCODING for enc in ("utf", "utf-8", "utf8"))


def _display_symbol(cell: str) -> str:
    """Retorna símbolo visual compatível com o terminal atual."""
    if cell == J1:
        return "●" if _SUPPORTS_UNICODE else "X"
    if cell == J2:
        return "●" if _SUPPORTS_UNICODE else "O"
    return "·" if _SUPPORTS_UNICODE else "."


def _piece_label(piece: str) -> str:
    return _display_symbol(piece)


def get_console() -> Console:
    """Retorna um Console rich adaptativo.

    - TTY detectado  → saída colorida/formatada (modo interativo).
    - Sem TTY        → texto plano sem ANSI (modo autograder/pipe).
    """
    return Console(force_terminal=_IS_TTY, highlight=False)


def render_board(
    board: list,
    console: Console,
    current_player: str | None = None,
    current_piece: str | None = None,
    last_col: int | None = None,
) -> None:
    """Exibe o tabuleiro no terminal.

    Em TTY usa uma tabela rich colorida; via pipe usa ASCII simples
    (uma linha por linha do tabuleiro + índices de coluna).
    """
    if _IS_TTY:
        # Espaçamento para separar visualmente cada estado do tabuleiro.
        console.print()

        if current_player is not None and current_piece is not None:
            console.print(
                f"[bold cyan]Turno:[/bold cyan] {current_player} "
                f"([bold]{_piece_label(current_piece)}[/bold])"
            )

        console.print(
            f"[dim]Legenda:[/dim] [bold red]{_display_symbol(J1)}[/bold red] "
            f"[dim]vs[/dim] [bold yellow]{_display_symbol(J2)}[/bold yellow]"
        )

        table = Table(box=box.SQUARE, show_header=True, header_style="bold cyan")
        for col in range(COLUNAS):
            is_selected_col = col == last_col
            header = str(col)
            header_style = "bold white on grey15" if is_selected_col else "bold cyan"
            table.add_column(header, justify="center", width=3, header_style=header_style)
        for row in board:
            cells = []
            for idx, cell in enumerate(row):
                symbol = _display_symbol(cell)
                if cell == J1:
                    style = "bold red"
                elif cell == J2:
                    style = "bold yellow"
                else:
                    style = "dim"

                if idx == last_col:
                    style += " on grey15"

                cells.append(Text(symbol, style=style))
            table.add_row(*cells)
        console.print(table)
    else:
        # Saída simples para autograding (sem ANSI)
        for row in board:
            print(" ".join(row))
        print(" ".join(str(c) for c in range(COLUNAS)))


def show_result(msg: str, console: Console) -> None:
    """Exibe a mensagem de fim de jogo com destaque (TTY) ou texto puro (pipe)."""
    if _IS_TTY:
        if "Empate" in msg:
            panel = Panel(msg, title="Fim de jogo", border_style="yellow")
        else:
            panel = Panel(msg, title="Fim de jogo", border_style="green")
        console.print()
        console.print(panel)
        console.print()
    else:
        print(msg)
