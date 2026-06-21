"""Exercício 10: Sistema de Empréstimo de Livros
=================================================
Implemente um sistema simplificado de controle de empréstimos de uma biblioteca.

O sistema começa com um acervo de N livros, todos disponíveis. Em seguida,
processa M operações sequenciais:

  EMPRESTAR titulo usuario  — empresta o livro ao usuário (se disponível).
                              Se o livro já estiver emprestado, exiba a mensagem
                              de indisponibilidade.
  DEVOLVER titulo           — marca o livro como disponível novamente.
  STATUS titulo             — exibe quem está com o livro, ou "disponivel".

Todos os nomes de livros e usuários são palavras únicas (sem espaços).

ENTRADA:
  Linha 1: inteiro N (número de livros, 1 <= N <= 20)
  Linhas 2..N+1: título de cada livro
  Linha N+2: inteiro M (número de operações, 1 <= M <= 50)
  Linhas N+3..N+M+2: operações no formato descrito acima

SAÍDA:
  Uma linha para cada operação STATUS ou tentativa de EMPRESTAR livro indisponível:
    STATUS disponível    → "titulo: disponivel"
    STATUS emprestado    → "titulo: usuario"
    EMPRESTAR indispon.  → "Indisponivel: titulo"

EXEMPLOS:
  Entrada:
    2
    Duna
    1984
    6
    EMPRESTAR Duna Alice
    STATUS Duna
    DEVOLVER Duna
    STATUS Duna
    EMPRESTAR 1984 Bruno
    STATUS 1984
  Saída:
    Duna: Alice
    Duna: disponivel
    1984: Bruno

  Entrada:
    1
    Sapiens
    4
    EMPRESTAR Sapiens Ana
    EMPRESTAR Sapiens Bruno
    STATUS Sapiens
    DEVOLVER Sapiens
  Saída:
    Indisponivel: Sapiens
    Sapiens: Ana

DICAS:
  - Represente o acervo como um dicionário: acervo[titulo] = None (disponível)
    ou acervo[titulo] = "usuario" (emprestado).
  - Para EMPRESTAR: verifique acervo[titulo] is None antes de emprestar.
  - Use linha.split() para separar os tokens da operação.
  - Para EMPRESTAR, a linha tem 3 tokens; para DEVOLVER e STATUS, 2 tokens.

CONTEÚDO: dicionários, None como sentinela, operações CRUD, estruturas condicionais
"""


def criar_acervo(titulos):
    """Cria o dicionário do acervo com todos os livros disponíveis.

    Parâmetro:
        titulos (list[str]): lista de títulos.

    Retorna:
        dict[str, str | None]: acervo com todos os livros mapeados para None.
    """
    pass


def processar_operacao(acervo, linha):
    """Processa uma operação e retorna a saída, se houver.

    Parâmetros:
        acervo (dict): dicionário do acervo.
        linha (str): string com a operação.

    Retorna:
        str | None: string a exibir, ou None se a operação não gera saída.
    """
    tokens = linha.split()
    operacao = tokens[0]

    if operacao == "EMPRESTAR":
        pass

    elif operacao == "DEVOLVER":
        pass

    elif operacao == "STATUS":
        pass

    return None


def main():
    n = int(input())
    titulos = [input().strip() for _ in range(n)]
    acervo = criar_acervo(titulos)

    m = int(input())
    for _ in range(m):
        saida = processar_operacao(acervo, input())
        if saida is not None:
            print(saida)


main()
