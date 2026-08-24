"""Exercício 09: Par de Pontos Mais Próximos
=============================================
Dados N pontos no plano cartesiano (com coordenadas inteiras), encontre
o par de pontos com a menor distância euclidiana entre si.

A distância entre dois pontos (x1, y1) e (x2, y2) é:
  d = sqrt((x2 - x1)² + (y2 - y1)²)

ENTRADA:
  Linha 1: inteiro N (quantidade de pontos, 2 <= N <= 50)
  Linhas 2..N+1: coordenadas "x y" de cada ponto (inteiros)

SAÍDA:
  Uma linha no formato:
    (x1, y1) (x2, y2) distancia: D.DD

  Onde (x1, y1) e (x2, y2) são os pontos do par mais próximo, e D.DD é
  a distância com exatamente 2 casas decimais.

  Critério de desempate (caso mais de um par tenha a mesma distância mínima):
    Exiba o par cujo primeiro ponto tem menor x; em caso de empate, menor y.
    O primeiro ponto do par é sempre o que aparece primeiro na entrada.

EXEMPLOS:
  Entrada:
    4
    0 0
    3 4
    1 1
    6 8
  Saída:
    (0, 0) (1, 1) distancia: 1.41

  Entrada:
    3
    0 0
    10 10
    0 1
  Saída:
    (0, 0) (0, 1) distancia: 1.00

DICAS:
  - Armazene cada ponto como uma tupla (x, y) em uma lista.
  - Use dois laços for aninhados: for i in range(N): for j in range(i+1, N):
  - Calcule a distância com math.sqrt(dx**2 + dy**2).
  - Mantenha variáveis para a menor distância encontrada e o par correspondente.
  - Para o desempate: ao achar uma distância igual, compare o par pelo primeiro ponto.

CONTEÚDO: tuplas, listas, laços aninhados, math.sqrt, comparação de tuplas
"""

import math


def par_mais_proximo(pontos):
    menor_dist = float("inf")
    melhor_par = None

    n = len(pontos)

    for i in range(n):
        for j in range(i + 1, n):
            p1 = pontos[i]
            p2 = pontos[j]

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            dist = math.sqrt(dx**2 + dy**2)

            if dist < menor_dist:
                menor_dist = dist
                melhor_par = (p1, p2)

            elif dist == menor_dist:
                if p1 < melhor_par[0]:
                    melhor_par = (p1, p2)

    return melhor_par[0], melhor_par[1], menor_dist


def main():
    n = int(input())

    pontos = []
    for _ in range(n):
        x, y = map(int, input().split())
        pontos.append((x, y))

    p1, p2, dist = par_mais_proximo(pontos)

    print(f"({p1[0]}, {p1[1]}) ({p2[0]}, {p2[1]}) distancia: {dist:.2f}")


main()