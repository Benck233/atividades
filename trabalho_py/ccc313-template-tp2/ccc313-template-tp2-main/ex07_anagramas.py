"""Exercício 07: Agrupador de Anagramas
========================================
Duas palavras são anagramas se uma pode ser formada rearranjando as letras
da outra (mesmas letras, mesma quantidade, ordem indiferente).

  Exemplos de grupos de anagramas:
    amor, maro, roma  →  todas têm as letras {a, m, o, r}
    arco, caro, orca  →  todas têm as letras {a, c, o, r}

Dado um conjunto de palavras, agrupe-as em grupos de anagramas e exiba
cada grupo em ordem.

ENTRADA:
  Linha 1: inteiro N (quantidade de palavras, 1 <= N <= 50)
  Linha 2: N palavras em minúsculas separadas por espaço

SAÍDA:
  Um grupo por linha. Dentro de cada grupo, as palavras aparecem em ordem
  alfabética crescente. Os grupos são ordenados pela primeira palavra de
  cada grupo (ordem alfabética crescente).

EXEMPLOS:
  Entrada:
    6
    amor roma maro caro arco orca
  Saída:
    amor maro roma
    arco caro orca

  Entrada:
    4
    ate eta tae sol
  Saída:
    ate eta tae
    sol

DICAS:
  - A "assinatura" de uma palavra é sua versão com letras ordenadas.
    Ex: "amor" → tuple(sorted("amor")) → ('a', 'm', 'o', 'r')
  - Use um dicionário onde a chave é a assinatura (tupla) e o valor
    é a lista de palavras com essa assinatura.
  - Tuplas podem ser chaves de dicionário; listas não.
  - Após agrupar, ordene as palavras dentro de cada grupo com sorted().
  - Ordene os grupos pela primeira palavra com sorted() e uma função auxiliar
    que retorna grupo[0].

CONTEÚDO: tuplas como chaves de dict, sorted(), agrupamento por chave
"""


def agrupar_anagramas(palavras):
    """Agrupa as palavras por anagrama."""
    grupos = {}

    for palavra in palavras:
        assinatura = tuple(sorted(palavra))

        if assinatura not in grupos:
            grupos[assinatura] = []

        grupos[assinatura].append(palavra)

    
    lista_grupos = []
    for grupo in grupos.values():
        lista_grupos.append(sorted(grupo))

    
    lista_grupos.sort(key=lambda grupo: grupo[0])

    return lista_grupos


def main():
    n = int(input())
    palavras = input().split()

    grupos = agrupar_anagramas(palavras)

    for grupo in grupos:
        print(*grupo)


main()
