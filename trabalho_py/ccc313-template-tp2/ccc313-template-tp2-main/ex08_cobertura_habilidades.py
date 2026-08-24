"""Exercício 08: Cobertura de Habilidades da Equipe
====================================================
Um projeto lista as habilidades técnicas necessárias. Cada membro da equipe
possui um conjunto próprio de habilidades. O objetivo é verificar se a equipe
como um todo cobre todas as habilidades exigidas.

ENTRADA:
  Linha 1: habilidades necessárias (palavras em maiúsculas separadas por espaço)
  Linha 2: inteiro N (número de membros da equipe, 1 <= N <= 10)
  Linhas 3..N+2: "Nome: habilidade1 habilidade2 ..."
    (nome não contém espaços; habilidades no mesmo formato que as necessárias)

SAÍDA:
  Se todas as habilidades necessárias estão cobertas:
    "Equipe completa"
  Caso contrário:
    "Habilidades faltando: h1 h2 h3" (em ordem alfabética)

EXEMPLOS:
  Entrada:
    Python SQL Docker
    3
    Ana: Python Docker
    Bruno: SQL Java
    Carlos: Go
  Saída:
    Equipe completa

  Entrada:
    Python SQL Docker Kubernetes
    2
    Ana: Python
    Bruno: SQL Java
  Saída:
    Habilidades faltando: Docker Kubernetes

DICAS:
  - Use set() para representar as habilidades necessárias.
  - Acumule todas as habilidades da equipe em um conjunto com for + .add().
  - A diferença de conjuntos (necessarias - disponiveis) dá as habilidades faltando.
  - Ordene as habilidades faltando com sorted() para saída determinística.
  - Para ler as habilidades de cada membro: linha.split(": ", 1) separa Nome de habilidades.

CONTEÚDO: conjuntos (set), operações de diferença, .add(), sorted()
"""


def verificar_cobertura(necessarias, membros):
    """Verifica quais habilidades necessárias não são cobertas pela equipe."""
    disponiveis = set()

    for membro in membros:
        nome, habilidades = membro.split(": ", 1)

        for habilidade in habilidades.split():
            disponiveis.add(habilidade)

    return necessarias - disponiveis


def main():
    necessarias = set(input().split())
    n = int(input())
    membros = [input() for _ in range(n)]

    faltando = verificar_cobertura(necessarias, membros)

    if len(faltando) == 0:
        print("Equipe completa")
    else:
        print("Habilidades faltando:", *sorted(faltando))


main()
