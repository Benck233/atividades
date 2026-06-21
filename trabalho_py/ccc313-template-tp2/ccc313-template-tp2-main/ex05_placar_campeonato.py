"""Exercício 05: Tabela do Campeonato
======================================
Processe os resultados de uma série de partidas de futebol e exiba a tabela
de classificação final ordenada pelos critérios oficiais.

Regras de pontuação:
  - Vitória: 3 pontos para o vencedor, 0 para o perdedor.
  - Empate:  1 ponto para cada time.

Critérios de desempate (em ordem):
  1. Maior número de pontos.
  2. Maior saldo de gols (gols pró menos gols contra).
  3. Nome do time em ordem alfabética (crescente).

ENTRADA:
  Linha 1: inteiro N (número de partidas, 1 <= N <= 50)
  Linhas 2..N+1: cada linha no formato "TimeA golsA golsB TimeB"
    (os nomes de times não contêm espaços)

SAÍDA:
  Uma linha por time, no formato "Posição. NomeTime Pontos", ex:
    1. Lobo 6
    2. Urso 4
    3. Gato 1

EXEMPLOS:
  Entrada:
    4
    Lobo 3 1 Gato
    Lobo 0 2 Urso
    Gato 1 1 Urso
    Lobo 2 0 Gato
  Saída:
    1. Lobo 6
    2. Urso 4
    3. Gato 1

  Entrada:
    3
    X 0 0 Y
    X 0 0 Z
    Y 1 0 Z
  Saída:
    1. Y 4
    2. X 2
    3. Z 1

DICAS:
  - Use um dicionário de dicionários: times[nome] = {"pts": 0, "gf": 0, "gc": 0}
  - Crie uma função auxiliar para garantir que o time existe no dict antes de atualizar.
  - Para ordenar a tabela com sorted(), monte tuplas no formato
    (-pontos, -saldo, nome, dados) e aplique sorted() nessa lista.
  - Use um contador de posição começando em 1 para numerar as linhas da classificação.

CONTEÚDO: dicionários aninhados, sorted(), tuplas para ordenação
"""


def registrar_time(times, nome):
    """Garante que o time existe no dicionário, inicializando com zeros."""
    pass


def processar_partida(times, linha):
    """Atualiza o dicionário de times com o resultado de uma partida.

    Parâmetro:
        linha (str): string no formato "TimeA golsA golsB TimeB"
    """
    partes = linha.split()
    time_a, gols_a, gols_b, time_b = partes[0], int(partes[1]), int(partes[2]), partes[3]

    registrar_time(times, time_a)
    registrar_time(times, time_b)
    pass


def classificar(times):
    """Retorna lista de (nome, dados) ordenada pelos critérios do campeonato."""
    pass


def main():
    n = int(input())
    times = {}

    for _ in range(n):
        processar_partida(times, input())

    ranking = classificar(times)
    pass


main()
