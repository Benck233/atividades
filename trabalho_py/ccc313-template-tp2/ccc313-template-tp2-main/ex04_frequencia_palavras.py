"""Exercício 04: Top-K Palavras Mais Frequentes
===============================================
Dado um texto e um número K, exiba as K palavras que aparecem com maior
frequência no texto. Em caso de empate na frequência, as palavras são
ordenadas alfabeticamente (A antes de B).

ENTRADA:
  Linha 1: o texto (uma única linha, palavras em minúsculas separadas por espaço)
  Linha 2: inteiro K (1 <= K <= número de palavras distintas)

SAÍDA:
  K linhas no formato "palavra: frequência", em ordem decrescente de frequência.
  Para frequências iguais, a palavra que vem primeiro no alfabeto aparece primeiro.

EXEMPLOS:
  Entrada:
    the quick brown fox jumps over the lazy dog the fox
    2
  Saída:
    the: 3
    fox: 2

  Entrada:
    a b c a b a c
    2
  Saída:
    a: 3
    b: 2

  (b e c têm frequência 2, mas b vem antes de c no alfabeto)

DICAS:
  - Use .split() para separar as palavras.
  - Use um dicionário para contar as frequências com passos explícitos:
      if palavra not in freq: freq[palavra] = 0
      freq[palavra] += 1
  - Para ordenar com sorted() sem algoritmo de ordenação manual,
    monte tuplas no formato (-frequência, palavra, frequência) e use sorted().
  - Fatie os K primeiros do resultado ordenado.

CONTEÚDO: dicionários, sorted(), tuplas para ordenação, .items()
"""


def top_k_palavras(texto, k):
    """Retorna as k palavras mais frequentes do texto como lista de tuplas.

    Parâmetros:
        texto (str): string com as palavras separadas por espaço.
        k (int): quantidade de palavras a retornar.

    Retorna:
        list[tuple[str, int]]: lista de (palavra, frequência), ordenada
            por frequência desc e nome asc para empates.
    """
    palavras = texto.split()

    freq = {}
    for palavra in palavras:
        if palavra not in freq:
            freq[palavra] = 0
        freq[palavra] += 1

    ordenado = []
    for palavra, frequencia in freq.items():
        ordenado.append((-frequencia, palavra, frequencia))

    ordenado = sorted(ordenado)

    resultado = []
    for _, palavra, frequencia in ordenado[:k]:
        resultado.append((palavra, frequencia))

    return resultado


def main():
    texto = input().strip()
    k = int(input().strip())

    resultado = top_k_palavras(texto, k)

    for palavra, frequencia in resultado:
        print(f"{palavra}: {frequencia}")


main()
