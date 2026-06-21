"""Exercício 06: Índice Invertido
==================================
Um índice invertido é uma estrutura fundamental em sistemas de busca:
para cada palavra, ele armazena a lista de documentos em que ela aparece.

Dado um conjunto de documentos e uma palavra de consulta, informe quais
documentos (por número, a partir de 1) contêm essa palavra.

ENTRADA:
  Linha 1: inteiro N (número de documentos, 1 <= N <= 20)
  Linhas 2..N+1: texto de cada documento (palavras em minúsculas, sem pontuação)
  Linha N+2: a palavra de consulta (uma única palavra, em minúsculas)

SAÍDA:
  Se a palavra for encontrada em pelo menos um documento:
    "Documentos: d1 d2 d3" (números em ordem crescente, separados por espaço)
  Caso contrário:
    "Nenhum documento encontrado"

EXEMPLOS:
  Entrada:
    3
    python e uma linguagem interpretada
    java e uma linguagem compilada
    python tambem tem suporte a orientacao
    python
  Saída:
    Documentos: 1 3

  Entrada:
    2
    linguagem de programacao funcional
    tipos estaticos em haskell
    python
  Saída:
    Nenhum documento encontrado

DICAS:
  - Construa o índice invertido como um dicionário:
      indice[palavra] = [1, 3, ...]  (lista de números de doc)
  - Ao processar cada documento (1-indexado), divida o texto em palavras
    e, para cada palavra, adicione o número do doc na lista correspondente.
  - Para buscar: use indice.get(query, []) para evitar KeyError.
  - Os números de documento já estarão em ordem crescente se você processar
    os documentos em sequência.

CONTEÚDO: dicionários com listas como valores, .get(), enumerate()
"""


def construir_indice(documentos):
    """Constrói o índice invertido a partir de uma lista de textos.

    Parâmetro:
        documentos (list[str]): lista de strings, cada uma com o texto de um doc.

    Retorna:
        dict[str, list[int]]: mapeamento palavra → lista de números de documento (1-indexed).
    """
    indice = {}
    return indice


def buscar(indice, query):
    """Retorna a lista de números de documentos que contêm query.

    Retorna lista vazia se a palavra não for encontrada.
    """
    pass


def main():
    n = int(input())
    documentos = [input() for _ in range(n)]
    query = input().strip()

    indice = construir_indice(documentos)
    resultado = buscar(indice, query)
    pass


main()
