
#70 para frente

import random
from datetime import date
from time import sleep
from operator import itemgetter

# 70. Número por Extenso
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {contagem[num]}')

# 71. Tuplas com Times de Futebol
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 
         'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(f'5 Primeiros: {times[:5]}')
print(f'4 Últimos: {times[-4:]}')
print(f'Ordem Alfabética: {sorted(times)}')
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')

# 72. Maior e menor valores em Tupla
numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), 
           random.randint(1, 10), random.randint(1, 10))
print(f'Valores: {numeros}')
print(f'Maior: {max(numeros)}, Menor: {min(numeros)}')

# 73. Análise de dados em uma Tupla
num = (int(input('N1: ')), int(input('N2: ')), int(input('N3: ')), int(input('N4: ')))
print(f'O 9 apareceu {num.count(9)} vezes')
if 3 in num: print(f'O 3 está na {num.index(3)+1}ª posição')
print(f'Pares: ', end='')
for n in num:
    if n % 2 == 0: print(n, end=' ')

# 74. Lista de Preços com Tupla
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

# 75. Contando vogais em Tupla
palavras = ('aprender', 'programar', 'linguagem', 'python')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# 76. Lista com nomes e pesos
temp = []
princ = []
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    temp.clear()
    resp = input('Continuar? [S/N] ')
    if resp in 'Nn': break
print(f'Cadastrados: {len(princ)}')

# 77. Valores únicos em uma Lista
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado! Não vou adicionar.')
    r = input('Continuar? [S/N] ')
    if r in 'Nn': break
numeros.sort()
print(f'Lista: {numeros}')

# 78. Lista ordenada sem repetições
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Ordem: {lista}')

# 79. Extraindo dados de uma Lista
valores = []
while True:
    valores.append(int(input('Valor: ')))
    if input('Continuar? [S/N] ') in 'Nn': break
print(f'Total: {len(valores)}')
valores.sort(reverse=True)
print(f'Decrescente: {valores}')
print(f'O 5 está na lista? {"Sim" if 5 in valores else "Não"}')

# 80. Dividindo valores em várias listas
num = []
pares = []
impares = []
while True:
    n = int(input('Valor: '))
    num.append(n)
    if n % 2 == 0: pares.append(n)
    else: impares.append(n)
    if input('Continuar? [S/N] ') in 'Nn': break
print(f'Tudo: {num}\nPares: {pares}\nÍmpares: {impares}')

# 81. Validando expressões matemáticas
expr = input('Digite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(': pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: pilha.pop()
        else: pilha.append(')')
print('Válida' if len(pilha) == 0 else 'Inválida')

# 82. Lista composta e análise de dados (Similar ao 76)
# [Implementação segue a lógica de listas dentro de listas]

# 83. Matriz em Python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

# 84. Mais sobre Matriz em Python
spar = scol3 = mlin2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0: spar += matriz[l][c]
        if c == 2: scol3 += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > mlin2: mlin2 = matriz[l][c]
print(f'Soma pares: {spar}\nSoma 3ª coluna: {scol3}\nMaior 2ª linha: {mlin2}')

# 85. Palpites para a Mega Sena
jogos = []
quant = int(input('Quantos jogos? '))
for c in range(0, quant):
    cont = 0
    lista = []
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6: break
    lista.sort()
    jogos.append(lista[:])
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

# 86. Boletim com listas compostas
ficha = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    ficha.append([nome, [n1, n2], (n1 + n2) / 2])
    if input('Continuar? [S/N] ') in 'Nn': break
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# 87. Dicionário em Python
aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média: '))
aluno['situacao'] = 'Aprovado' if aluno['media'] >= 7 else 'Reprovado'
print(f'O aluno {aluno["nome"]} está {aluno["situacao"]}')

# 88. Jogo de Dados em Python
jogo = {'J1': random.randint(1, 6), 'J2': random.randint(1, 6), 
        'J3': random.randint(1, 6), 'J4': random.randint(1, 6)}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

# 89. Cadastro de Trabalhador
dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano Nasc: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('CTPS (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - date.today().year)
print(dados)

# 90. Cadastro de Jogador de Futebol
jogador = {}
partidas = []
jogador['nome'] = input('Nome: ')
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)

# 91. Unindo dicionários e listas
galera = []
pessoa = {}
soma = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    if input('Continuar? [S/N] ') in 'Nn': break
print(f'Cadastrados: {len(galera)}\nMédia Idade: {soma/len(galera):.2f}')

# 92. Aprimorando os Dicionários (Versão múltipla do 90)
# [Lógica: Adicionar o dicionário do jogador em uma lista e usar um loop para exibir]

# 93. Função que calcula área
def area(larg, comp):
    a = larg * comp
    print(f'A área de {larg}x{comp} é {a}m²')

# 94. Um print especial
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# 95. Função de Contador
def contador(i, f, p):
    if p < 0: p *= -1
    if p == 0: p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
    print('FIM!')

# 96. Função que descobre o maior
def maior(* num):
    m = 0
    for valor in num:
        if valor > m: m = valor
    print(f'O maior valor foi {m}')

# 97. Funções para sortear e somar
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(random.randint(1, 10))

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0: soma += v
    print(f'Soma dos pares de {lista}: {soma}')

# 98. Funções para votação
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16: return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65: return f'Com {idade} anos: VOTO OPCIONAL.'
    else: return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# 99. Função para Fatorial
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f

# 100. Projeto Final (Exemplo: Sistema de Notas)
def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7: r['situacao'] = 'BOA'
        elif r['media'] >= 5: r['situacao'] = 'RAZOÁVEL'
        else: r['situacao'] = 'RUIM'
    return r