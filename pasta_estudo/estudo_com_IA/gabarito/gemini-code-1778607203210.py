
#do 36 até 70


import random
from datetime import date
from time import sleep
from operator import itemgetter

# 36. Comparando números
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')

# 37. Alistamento Militar
da_nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - da_nasc
if idade == 18:
    print('É a hora exata de se alistar!')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para o alistamento.')
else:
    print(f'Já passou o tempo do alistamento há {idade - 18} anos.')

# 38. Média
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m < 5.0: print('REPROVADO')
elif 5.0 <= m <= 6.9: print('RECUPERAÇÃO')
else: print('APROVADO')

# 39. Classificando Atletas
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
if idade <= 9: print('MIRIM')
elif idade <= 14: print('INFANTIL')
elif idade <= 19: print('JUNIOR')
elif idade <= 25: print('SÊNIOR')
else: print('MASTER')

# 40. Analisando Triângulos v2.0
s1 = float(input('Lado 1: '))
s2 = float(input('Lado 2: '))
s3 = float(input('Lado 3: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3: print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1: print('ESCALENO')
    else: print('ISÓSCELES')
else: print('Não formam um triângulo.')

# 41. IMC
p = float(input('Peso (kg): '))
a = float(input('Altura (m): '))
imc = p / (a ** 2)
if imc < 18.5: print('Abaixo do Peso')
elif 18.5 <= imc < 25: print('Peso Ideal')
elif 25 <= imc < 30: print('Sobrepeso')
elif 30 <= imc < 40: print('Obesidade')
else: print('Obesidade Mórbida')

# 42. Gerenciador de Pagamentos
preco = float(input('Preço: R$'))
print('[1] à vista / [2] cartão / [3] 2x cartão / [4] 3x+ cartão')
op = int(input('Opção: '))
if op == 1: print(f'Total: R${preco*0.9:.2f}')
elif op == 2: print(f'Total: R${preco*0.95:.2f}')
elif op == 3: print(f'Total: R${preco:.2f}')
elif op == 4: print(f'Total: R${preco*1.2:.2f}')

# 43. Jokenpô (Simplificado)
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
jogador = int(input('0-Pedra, 1-Papel, 2-Tesoura: '))
print(f'PC jogou {itens[pc]}')
if pc == jogador: print('EMPATE')
elif (pc == 0 and jogador == 1) or (pc == 1 and jogador == 2) or (pc == 2 and jogador == 0): print('VOCÊ VENCEU')
else: print('PC VENCEU')

# 44. Contagem regressiva
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!')

# 45. Contagem de pares
for n in range(2, 51, 2):
    print(n, end=' ')

# 46. Soma ímpares múltiplos de três
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(f'A soma é {s}')

# 47. Tabuada v.2.0
n = int(input('Número: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')

# 48. Soma dos pares
s = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0: s += num
print(f'Soma dos pares: {s}')

# 49. Progressão Aritmética
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(0, 10):
    print(f'{termo}', end=' -> ')
    termo += razão
print('FIM')

# 50. Números primos
num = int(input('Número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0: tot += 1
if tot == 2: print('É PRIMO')
else: print('NÃO É PRIMO')

# 51. Detector de Palíndromo
frase = input('Frase: ').strip().upper().replace(' ', '')
if frase == frase[::-1]: print('É um palíndromo')
else: print('Não é palíndromo')

# 52. Grupo da Maioridade
maiores = 0
for p in range(1, 8):
    nasc = int(input(f'Ano {p}: '))
    if date.today().year - nasc >= 18: maiores += 1
print(f'{maiores} são maiores e {7-maiores} são menores.')

# 53. Maior e menor da sequência
pesos = []
for p in range(1, 6):
    pesos.append(float(input(f'Peso {p}: ')))
print(f'Maior: {max(pesos)}kg, Menor: {min(pesos)}kg')

# 54. Analisador completo
soma_idade = 0
homem_velho = ''
idade_homem = 0
mulheres_20 = 0
for p in range(1, 5):
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').upper()
    soma_idade += i
    if s == 'M' and i > idade_homem:
        idade_homem = i
        homem_velho = n
    if s == 'F' and i < 20: mulheres_20 += 1
print(f'Média idade: {soma_idade/4}')
print(f'Homem mais velho: {homem_velho}')
print(f'Mulheres < 20 anos: {mulheres_20}')

# 55. Validação de Dados
sexo = input('Sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]

# 56. Jogo da Adivinhação v2.0
pc = randint(0, 10)
tentativas = 0
acertou = False
while not acertou:
    p = int(input('Palpite (0-10): '))
    tentativas += 1
    if p == pc: acertou = True
    else: print('Errou! Tente novamente.')
print(f'Acertou com {tentativas} tentativas.')

# 57. Criando um Menu de Opções
op = 0
n1 = int(input('N1: '))
n2 = int(input('N2: '))
while op != 5:
    print('[1]Somar [2]Mult [3]Maior [4]Novos [5]Sair')
    op = int(input('Opção: '))
    if op == 1: print(n1 + n2)
    elif op == 2: print(n1 * n2)
    elif op == 3: print(max(n1, n2))
    elif op == 4: n1 = int(input('N1: ')); n2 = int(input('N2: '))

# 58. Cálculo do Fatorial
from math import factorial
n = int(input('Número: '))
print(f'Fatorial: {factorial(n)}')

# 59. PA v2.0
t = int(input('Termo: '))
r = int(input('Razão: '))
c = 1
while c <= 10:
    print(t, end=' ')
    t += r
    c += 1

# 60. PA v3.0
t = int(input('Termo: '))
r = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(t, end=' ')
        t += r
        c += 1
    mais = int(input('\nQuantos termos mais? '))

# 61. Fibonacci
n = int(input('Termos: '))
t1, t2 = 0, 1
c = 3
print(f'{t1} -> {t2}', end='')
while c <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1

# 62/64. Tratando valores (Flag 999)
num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Digitou {cont} números e a soma foi {soma}.')

# 63. Médias, Maior e Menor
resp = 'S'
soma = cont = 0
valores = []
while resp in 'SS':
    n = int(input('Número: '))
    soma += n
    cont += 1
    valores.append(n)
    resp = input('Continuar? [S/N] ').upper()
print(f'Média: {soma/cont}, Maior: {max(valores)}, Menor: {min(valores)}')

# 65. Tabuada v3.0
while True:
    n = int(input('Tabuada de qual valor? '))
    if n < 0: break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')