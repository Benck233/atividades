"""Exercício 11: Menor Caminho em Grafo — BFS
==============================================
Dado um grafo não-dirigido e não-ponderado, use Busca em Largura (BFS) para
encontrar o número mínimo de arestas entre dois vértices.

Na BFS, exploramos primeiro todos os vértices a distância 1 da origem,
depois os a distância 2, e assim por diante — garantindo o menor caminho.

ENTRADA:
  Linha 1: dois inteiros V e E (vértices e arestas, 2 <= V <= 20, 1 <= E <= 50)
  Linhas 2..E+1: "A B" (aresta entre A e B; o grafo é não-dirigido)
  Linha E+2: "origem destino" (os dois vértices para a consulta)

  Os nomes de vértices são letras maiúsculas (A, B, C, ...).

SAÍDA:
  O número mínimo de arestas no caminho entre origem e destino.
  Ou "Sem caminho" se não existir caminho.

EXEMPLOS:
  Entrada:
    4 4
    A B
    B C
    C D
    A C
    A D
  Saída:
    2

  Explicação: A→C→D usa 2 arestas (A→B→C→D usaria 3; A→C→D é mais curto).

  Entrada:
    4 2
    A B
    C D
    A D
  Saída:
    Sem caminho

  (A e D estão em componentes desconexos.)

DICAS:
  - Represente o grafo como um dicionário de conjuntos:
      grafo[v] = set() de vizinhos.
  - Para cada aresta A-B, adicione B em grafo[A] e A em grafo[B].
  - BFS com lista como fila: fila = [(origem, 0)] e use fila.pop(0).
  - Mantenha um conjunto 'visitados' para não revisitar vértices.
  - Quando alcançar o destino, retorne a distância atual + 1.

ALGORITMO BFS:
  1. visitados = {origem}; fila = [(origem, 0)]
  2. Enquanto fila não vazia:
       (vertice, dist) = fila.pop(0)
       Para cada vizinho em grafo.get(vertice, set()):
         Se vizinho == destino: retorne dist + 1
         Se vizinho não visitado: adicione a visitados e à fila com dist + 1
  3. Se fila esvaziar sem achar destino: retorne -1 (sem caminho)

CONTEÚDO: dicionários de conjuntos, BFS, listas como fila, grafos
"""


def construir_grafo(arestas):
    """Constrói o grafo como dicionário de conjuntos.

    Parâmetro:
        arestas (list[str]): lista de strings "A B".

    Retorna:
        dict[str, set[str]]: adjacência do grafo não-dirigido.
    """
    grafo = {}
    return grafo


def bfs(grafo, origem, destino):
    """Retorna a distância mínima (em arestas) entre origem e destino.

    Retorna -1 se não houver caminho.
    """
    if origem == destino:
        return 0
    pass


def main():
    v, e = map(int, input().split())
    arestas = [input() for _ in range(e)]
    origem, destino = input().split()

    grafo = construir_grafo(arestas)
    distancia = bfs(grafo, origem, destino)

    if distancia == -1:
        print("Sem caminho")
    else:
        print(distancia)


main()
