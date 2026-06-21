"""Exercício 12: Cache LRU Simplificado
========================================
Um cache LRU (Least Recently Used) é uma estrutura de dados que armazena
um número limitado de itens. Quando o cache está cheio e um novo item precisa
ser inserido, o item menos recentemente utilizado (o que não é acessado há
mais tempo) é removido.

Um item é considerado "utilizado" em uma operação PUT (inserção/atualização)
ou GET (leitura).

OPERAÇÕES:
  PUT chave valor — insere ou atualiza o par (chave, valor) no cache.
                    Se o cache estiver cheio, remove o item LRU antes de inserir.
  GET chave       — retorna o valor associado à chave.
                    Se a chave não existir no cache: exibe "Nenhum".

Tanto chaves quanto valores são inteiros não-negativos.

ENTRADA:
  Linha 1: inteiro C (capacidade do cache, 1 <= C <= 10)
  Linha 2: inteiro N (número de operações, 1 <= N <= 30)
  Linhas 3..N+2: operações "PUT chave valor" ou "GET chave"

SAÍDA:
  Uma linha para cada operação GET, com o valor encontrado ou "Nenhum".

EXEMPLOS:
  Entrada:
    2
    6
    PUT 1 100
    PUT 2 200
    GET 1
    PUT 3 300
    GET 2
    GET 1
  Saída:
    100
    Nenhum
    100

  Trace:
    PUT 1→100: cache={1:100}, recentes=[1]
    PUT 2→200: cache={1:100, 2:200}, recentes=[1, 2]
    GET 1: retorna 100, recentes=[2, 1]  (1 vira o mais recente)
    PUT 3→300: cache cheio, remove LRU=2, cache={1:100, 3:300}, recentes=[1, 3]
    GET 2: 2 não está no cache → "Nenhum"
    GET 1: retorna 100 → "100"

  Entrada:
    3
    3
    PUT 1 10
    PUT 2 20
    GET 5
  Saída:
    Nenhum

DICAS:
  - Use duas estruturas em conjunto:
      cache (dict): chave → valor, para busca em O(1).
      recentes (list): lista de chaves em ordem de uso (índice 0 = LRU, -1 = MRU).
  - Para GET e PUT de chave já existente: remova a chave de recentes
    (use recentes.remove(chave)) e reinsira no final (recentes.append(chave)).
  - Para PUT de nova chave quando cache cheio:
      antigo = recentes.pop(0)   # remove o LRU
      del cache[antigo]
  - Inicialize recentes = [] e cache = {}.

CONTEÚDO: dicionários + listas combinados, política de evicção, simulação de estado
"""


def main():
    capacidade = int(input())
    n = int(input())

    cache = {}       # chave → valor
    recentes = []    # lista de chaves: recentes[0] = LRU, recentes[-1] = MRU

    for _ in range(n):
        partes = input().split()
        operacao = partes[0]

        if operacao == "PUT":
            chave = int(partes[1])
            valor = int(partes[2])

            pass

        elif operacao == "GET":
            chave = int(partes[1])

            pass


main()
