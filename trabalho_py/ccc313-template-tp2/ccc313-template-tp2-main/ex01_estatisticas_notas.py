"""Exercício 01: Estatísticas de Notas da Turma
================================================
Dado um conjunto de N notas de alunos, calcule e exiba:
  - A menor nota da turma
  - A maior nota da turma
  - A mediana das notas
  - O número de alunos aprovados (nota >= 6.0)

A MEDIANA é o valor central de uma lista ordenada:
  - Se N for ímpar: é o elemento do meio.
  - Se N for par: é a MÉDIA dos dois elementos centrais.

ENTRADA:
  Linha 1: inteiro N (quantidade de notas, 1 <= N <= 100)
  Linha 2: N números reais separados por espaço (as notas, entre 0.0 e 10.0)

SAÍDA:
  Quatro linhas, nesta ordem:
    Menor: X.X
    Maior: X.X
    Mediana: X.X
    Aprovados: K

  Todos os valores numéricos com exatamente 1 casa decimal.

EXEMPLOS:
  Entrada:
    5
    7.0 4.5 9.0 6.5 8.0
  Saída:
    Menor: 4.5
    Maior: 9.0
    Mediana: 7.0
    Aprovados: 4

  Entrada:
    4
    5.0 3.0 7.0 9.0
  Saída:
    Menor: 3.0
    Maior: 9.0
    Mediana: 6.0
    Aprovados: 2

DICAS:
  - Use sorted() para ordenar as notas.
  - O índice do elemento central (N ímpar) é N // 2.
  - Para N par, os centrais são os índices N//2 - 1 e N//2.
  - Itere a lista com um for para contar aprovados.

CONTEÚDO: listas, sorted(), slicing, enumerate, len()
"""


def calcular_estatisticas(notas):
    """Calcula menor, maior, mediana e aprovados a partir da lista de notas.

    Parâmetros:
        notas (list[float]): lista com as notas da turma.

    Retorna:
        tuple: (menor, maior, mediana, aprovados)
    """

    maior_nota=notas[0]
    menor_nota=notas[0]

    for nota in notas:
      if nota < menor_nota:
         menor_nota= nota
      
      if nota > maior_nota:
         maior_nota=nota
    
    sorted(notas)

    mediana=0
    if len(notas) %2 == 0:
      n= len(notas)
      
      mediana= (notas[(n//2 - 1)] + notas[n//2])/2
    else:
       n= len(notas)
       mediana=notas[n//2]

    aluno_aprovado=0

    for nota_aluno in notas:
       if nota_aluno >=6.0:
          aluno_aprovado= aluno_aprovado + 1.0
          
    return(menor_nota, maior_nota, mediana, aluno_aprovado)
   # pass


def main():
    n = int(input())
    notas = list(map(float, input().split()))

    menor, maior, mediana, aprovados = calcular_estatisticas(notas)
    print(f"Menor: {menor:.1f}")
    print(f"Maior: {maior:.1f}")
    print(f"Mediana: {mediana:.1f}")
    print(f"Aprovados: {aprovados:.0f}")
    #pass


main()
