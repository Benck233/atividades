# Dicas Complementares — TP2

Este arquivo traz mini-tutoriais sobre os recursos do Python usados nos exercícios.
Leia antes de começar — você vai precisar de pelo menos dois deles em cada exercício.

---

## 1. `sorted()` — ordenação sem escrever algoritmo

Em Python você nunca precisa implementar um algoritmo de ordenação do zero.
A função embutida `sorted()` já faz isso.

### 1.1 Uso básico

```python
notas = [7.0, 4.5, 9.0, 6.5, 8.0]

ordenadas   = sorted(notas)               # crescente: [4.5, 6.5, 7.0, 8.0, 9.0]
decrescente = sorted(notas, reverse=True) # decrescente: [9.0, 8.0, 7.0, 6.5, 4.5]
```

`sorted()` **sempre retorna uma nova lista**; a lista original não é alterada.

### 1.2 Múltiplos critérios de ordenação com tuplas

Para ordenar por mais de um critério (ex.: nota decrescente e, em empate, nome
alfabético), o padrão é montar uma lista de tuplas em que cada tupla começa com
os critérios de ordenação, e depois chamar `sorted()` sobre essa lista.

O Python compara tuplas elemento por elemento, da esquerda para a direita.
O **sinal negativo** em um número inverte a ordem só daquele campo:

```python
alunos = [("Carlos", 7.5), ("Ana", 9.0), ("Bruno", 7.5)]

base = []
for nome, nota in alunos:
    base.append((-nota, nome, nota))   # (-nota, nome, nota)
    #            ^^^^^ critério 1: nota decrescente
    #                   ^^^^ critério 2: nome crescente (em empate)

base = sorted(base)
# base: [(-9.0,'Ana',9.0), (-7.5,'Bruno',7.5), (-7.5,'Carlos',7.5)]

# Para extrair os dados após ordenar:
for _, nome, nota in base:
    print(nome, nota)
# Ana 9.0
# Bruno 7.5
# Carlos 7.5
```

Esse padrão aparece nos exercícios 04 e 05.

### 1.3 Usando `key` com uma função auxiliar

Quando você quiser ordenar uma lista por apenas um campo específico de cada
elemento, use o parâmetro `key` com uma função que extrai esse campo:

```python
def primeira_palavra(grupo):
    return grupo[0]

grupos = [["roma", "amor"], ["sol"], ["ate", "eta"]]
grupos_ordenados = sorted(grupos, key=primeira_palavra)
# [['ate', 'eta'], ['roma', 'amor'], ['sol']]
```

Esse padrão aparece no exercício 07, para ordenar os grupos de anagramas.

### 1.4 `sorted()` aplicado a uma string

`sorted()` funciona sobre qualquer sequência, inclusive strings. Sobre uma string,
ele retorna uma lista com as letras em ordem alfabética:

```python
sorted("amor")          # ['a', 'm', 'o', 'r']
tuple(sorted("amor"))   # ('a', 'm', 'o', 'r')
```

Isso é o que permite identificar anagramas no exercício 07: duas palavras são
anagramas se e somente se `tuple(sorted(palavra1)) == tuple(sorted(palavra2))`.

---

## 2. Tuplas como chaves de dicionário

Dicionários exigem que as chaves sejam **imutáveis**. Strings e números são
imutáveis. Tuplas também são imutáveis e por isso **podem** ser chaves.
Listas **não podem** ser chaves.

```python
grupos = {}

chave = tuple(sorted("amor"))     # ('a', 'm', 'o', 'r')
grupos[chave] = ["amor", "maro"]  # OK ✓

grupos[["a", "m", "o", "r"]] = [] # TypeError — lista não pode ser chave ✗
```

Padrão para agrupar palavras pela assinatura de letras (exercício 07):

```python
grupos = {}
for palavra in palavras:
    chave = tuple(sorted(palavra))
    if chave not in grupos:
        grupos[chave] = []
    grupos[chave].append(palavra)
```

---

## 3. Conjuntos (`set`)

Conjuntos armazenam elementos **sem repetição** e permitem testar pertencimento
de forma eficiente.

### 3.1 Criação

```python
habilidades = {"Python", "SQL", "Docker"}  # com elementos
visitados   = set()                         # VAZIO — use set(), não {}
                                            # {} sozinho cria dicionário vazio!
```

### 3.2 Adicionar e testar pertencimento

```python
visitados = set()
visitados.add("A")
visitados.add("A")   # duplicata ignorada silenciosamente
# visitados → {'A'}

if "B" not in visitados:
    visitados.add("B")
```

### 3.3 Diferença de conjuntos

A diferença `a - b` retorna os elementos que estão em `a` mas não estão em `b`:

```python
necessarias = {"Python", "SQL", "Docker"}
disponiveis = {"Python", "Java"}

faltando = necessarias - disponiveis
# faltando → {'SQL', 'Docker'}
```

Isso é o que o exercício 08 pede para verificar as habilidades ausentes na equipe.

---

## 4. `split()` e `join()` — converter entre string e lista

### 4.1 `split()` — dividir uma string em partes

```python
"2 1 5 3 6".split()              # ['2', '1', '5', '3', '6']  — divide por espaços
"Ana: Python Docker".split()     # ['Ana:', 'Python', 'Docker']

# Com separador explícito e limite de divisões:
"Ana: Python Docker".split(": ", 1)  # ['Ana', 'Python Docker']
#                              ^ limita a no máximo 1 divisão
```

O segundo exemplo com `split(": ", 1)` aparece no exercício 08 para separar o
nome do membro das suas habilidades.

### 4.2 `join()` — juntar uma lista em string

```python
" ".join(["ate", "eta", "tae"])  # "ate eta tae"
"".join(["3a", "2b", "4c"])      # "3a2b4c"
```

Para juntar uma lista de inteiros, converta cada elemento com `str()` primeiro:

```python
resultado = [5, 5, 6, 6]
" ".join(str(x) for x in resultado)   # "5 5 6 6"
```

### 4.3 Nota: `map()` nos templates

Alguns `main()` já fornecidos nos arquivos de template usam `map()`:

```python
n, k = map(int, input().split())           # lê dois inteiros de uma linha
nums = list(map(int, input().split()))     # lê uma lista de inteiros
```

`map(int, lista_de_strings)` converte cada string para int. Você não precisa
escrever `map()` nas suas implementações — ela já aparece no código de leitura
pronto —, mas é útil saber o que ela faz ao ler os templates.

---

## 5. `None` como sentinela

Usar `None` para representar "ausência de valor" é um padrão comum em Python.
No exercício 10, `None` indica que um livro está disponível (sem usuário):

```python
acervo = {"Duna": None, "1984": None}   # None = disponível

# Verificar se está disponível e emprestar
if acervo["Duna"] is None:
    acervo["Duna"] = "Alice"            # agora emprestado para Alice

# Verificar se está emprestado
if acervo["Duna"] is not None:
    print(f"Duna: {acervo['Duna']}")    # Duna: Alice
```

Use sempre `is None` e `is not None` (não `== None`).

---

## 6. Listas como fila (FIFO)

Uma fila processa elementos na ordem em que chegaram: o primeiro a entrar é o
primeiro a sair. Com listas do Python:

```python
fila = []
fila.append("A")        # inserir no final
fila.append("B")
primeiro = fila.pop(0)  # remover e retornar o primeiro: "A"
```

No exercício 11 (BFS), a fila guarda tuplas `(vértice, distância)`:

```python
fila = [(origem, 0)]
while fila:
    vertice, dist = fila.pop(0)
    for vizinho in grafo[vertice]:
        fila.append((vizinho, dist + 1))
```

No exercício 12 (Cache LRU), a lista de recentes usa a mesma mecânica:
`pop(0)` remove o menos recente e `append()` marca um item como o mais recente.

---

## 7. Testando localmente no terminal

Para passar várias linhas de entrada a um script sem digitá-las manualmente:

```bash
printf "5\n7.0 4.5 9.0 6.5 8.0\n" | python ex01_estatisticas_notas.py
```

`printf` interpreta `\n` como quebra de linha tanto no bash quanto no zsh.
Não use `echo "...\n..."` no macOS — o zsh não interpreta `\n` dessa forma.

Para entradas maiores, salve em um arquivo de texto e redirecione:

```bash
# salvar a entrada em um arquivo
printf "4\nLobo 3 1 Gato\nLobo 0 2 Urso\nGato 1 1 Urso\nLobo 2 0 Gato\n" > entrada.txt

# rodar o script lendo desse arquivo
python ex05_placar_campeonato.py < entrada.txt
```

---

## 8. Depuração com `print` temporário

Quando a saída não bater com o esperado, adicione prints para inspecionar
variáveis intermediárias. Use `stderr` para não misturar com a saída do programa:

```python
import sys

print("DEBUG:", variavel, file=sys.stderr)
```

A saída de `stderr` aparece no terminal mas **não** entra na comparação do
autograder. Lembre-se de remover as linhas de debug antes de fazer `push`.