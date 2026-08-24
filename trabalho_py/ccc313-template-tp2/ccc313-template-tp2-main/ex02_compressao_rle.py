"""Exercício 02: Compressão e Descompressão RLE
================================================
Run-Length Encoding (RLE) é uma técnica simples de compressão que substitui
sequências de caracteres repetidos pelo número de repetições seguido do
caractere.

  Exemplos:
    "aaabbbccddddee" → "3a3b2c4d2e"
    "abcd"           → "1a1b1c1d"

Este programa opera em dois modos:
  C (Comprimir)   — transforma a string original na versão comprimida.
  D (Descomprimir) — restaura a string original a partir da versão comprimida.

O formato comprimido garante que cada grupo começa com um inteiro positivo
(pode ter mais de um dígito) seguido de exatamente um caractere.

ENTRADA:
  Linha 1: "C" ou "D" (modo de operação)
  Linha 2: a string a ser processada

SAÍDA:
  Uma linha com o resultado da operação.

EXEMPLOS:
  Entrada:
    C
    aaabbbccddddee
  Saída:
    3a3b2c4d2e

  Entrada:
    D
    3a3b2c4d2e
  Saída:
    aaabbbccddddee

DICAS PARA COMPRESSÃO:
  - Percorra a string comparando cada caractere com o anterior.
  - Mantenha um contador que reseta sempre que o caractere muda.
  - Acumule os pares "NúmeroChar" em uma lista e junte com "".join().

DICAS PARA DESCOMPRESSÃO:
  - Use um índice i para percorrer a string comprimida manualmente (while).
  - Enquanto s[i].isdigit(), acumule os dígitos para formar o número.
  - O próximo caractere (não dígito) é o char a ser repetido.

CONTEÚDO: listas, strings, indexação, while, append, join
"""


def comprimir(s):
    """Aplica compressão RLE na string s.

    Parâmetro:
        s (str): string original (não vazia).

    Retorna:
        str: string comprimida no formato "NúmeroChar...".
    """
    resultado=[]

    contador=1

    for i in range(1,len(s)):
        
      if s[i] == s[i-1]:
        contador+=1
      else:
         resultado.append(str(contador))
         resultado.append(s[i-1])
         contador=1

    resultado.append(str(contador))
    resultado.append(s[-1])

    return "".join(resultado)


    #pass


def descomprimir(s):
    """Desfaz a compressão RLE da string s.

    Parâmetro:
        s (str): string comprimida no formato "NúmeroChar...".

    Retorna:
        str: string original restaurada.
    """
    resultado=[]
    i=0

    while i < len(s) and s[i].isdigit():
      numero = ""

      while i < len(s) and s[i].isdigit():
        numero+= s[i]
        i+=i

      quantidade = int(numero)
      caractere =s[i]

      resultado.append(caractere*quantidade)
      i+=1

    return"".join(resultado)
    #pass


def main():
    modo = input().strip()
    texto = input().strip()

    if modo == "C":
        print(comprimir(texto))
    else:
        print(descomprimir(texto))


main()
