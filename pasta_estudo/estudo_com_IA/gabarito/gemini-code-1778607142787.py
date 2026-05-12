
#De 0 a 30

import math
from datetime import date
from random import randint

# 01
print("Olá, Mundo!")

# 02
nome = input("Digite seu nome: ")
print(f"Olá {nome}, seja bem-vindo!")

# 03
n1 = int(input("N1: "))
n2 = int(input("N2: "))
print(f"Soma: {n1 + n2}")

# 04
n = int(input("Número: "))
print(f"Antecessor: {n-1}, Sucessor: {n+1}")

# 05
n = float(input("Número: "))
print(f"Dobro: {n*2}, Triplo: {n*3}, Raiz: {n**(1/2):.2f}")

# 06
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
print(f"Média: {(n1+n2)/2}")

# 07
m = float(input("Metros: "))
print(f"{m}m são {m*100}cm e {m*1000}mm")

# 08
n = int(input("Tabuada de: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 09
real = float(input("R$: "))
print(f"Você pode comprar US${real/5:.2f}")

# 10
l = float(input("Largura: "))
a = float(input("Altura: "))
area = l * a
print(f"Área: {area}m². Tinta: {area/2}L")

# 11
p = float(input("Preço: "))
print(f"Com 5% de desconto: {p*0.95:.2f}")

# 12
s = float(input("Salário: "))
print(f"Com 15% de aumento: {s*1.15:.2f}")

# 13
c = float(input("°C: "))
print(f"°F: {(c*9/5)+32}")

# 14
dias = int(input("Dias: "))
km = float(input("Km: "))
pago = (dias * 60) + (km * 0.15)
print(f"Total: R${pago:.2f}")

# 15
num = float(input("Valor Real: "))
print(f"Parte inteira: {int(num)}")

# 16
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
hi = math.hypot(co, ca)
print(f"Hipotenusa: {hi:.2f}")

# 17
an = float(input("Ângulo: "))
rad = math.radians(an)
print(f"Seno: {math.sin(rad):.2f}, Cosseno: {math.cos(rad):.2f}, Tangente: {math.tan(rad):.2f}")

# 18
nomes = [input("N1: "), input("N2: "), input("N3: "), input("N4: ")]
import random
print(f"Escolhido: {random.choice(nomes)}")

# 19
random.shuffle(nomes)
print(f"Ordem: {nomes}")

# 20
nome = input("Nome completo: ").strip()
print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"Letras ao todo: {len(nome) - nome.count(' ')}")
print(f"Letras primeiro nome: {len(nome.split()[0])}")

# 21
num = int(input("0-9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"U:{u} D:{d} C:{c} M:{m}")

# 22
cid = input("Cidade: ").strip()
print(cid[:5].upper() == 'SANTO')

# 23
n = input("Nome: ").strip()
print(f"Silva? {'SILVA' in n.upper()}")

# 24
frase = input("Frase: ").upper().strip()
print(f"A aparece {frase.count('A')} vezes")
print(f"Primeira: {frase.find('A')+1}")
print(f"Última: {frase.rfind('A')+1}")

# 25
n = input("Nome: ").strip().split()
print(f"Primeiro: {n[0]}, Último: {n[-1]}")

# 26
cpu = randint(0, 5)
player = int(input("Pensei num número de 0 a 5. Qual foi? "))
print("Venceu!" if cpu == player else f"Perdeu! Era {cpu}")

# 27
v = float(input("Velocidade: "))
if v > 80:
    print(f"Multado! Valor: R${(v-80)*7:.2f}")

# 28
n = int(input("Número: "))
print("Par" if n % 2 == 0 else "Ímpar")

# 29
dist = float(input("Distância: "))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f"Passagem: R${preco:.2f}")

# 30
ano = int(input("Ano (0 para atual): "))
if ano == 0: ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")