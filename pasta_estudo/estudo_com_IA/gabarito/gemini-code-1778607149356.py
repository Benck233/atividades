# 31
a, b, c = int(input()), int(input()), int(input())
print(f"Maior: {max(a, b, c)}, Menor: {min(a, b, c)}")

# 32
sal = float(input("Salário: "))
aum = sal * 0.10 if sal > 1250 else sal * 0.15
print(f"Novo salário: R${sal + aum:.2f}")

# 33
r1, r2, r3 = float(input()), float(input()), float(input())
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podem formar triângulo")
else:
    print("Não podem")

# 34
casa = float(input("Valor casa: "))
sal = float(input("Salário: "))
anos = int(input("Anos: "))
prest = casa / (anos * 12)
if prest <= sal * 0.3:
    print("Aprovado")
else:
    print("Negado")

# 35
num = int(input("Inteiro: "))
esc = int(input("1-Bin 2-Oct 3-Hex: "))
if esc == 1: print(bin(num)[2:])
elif esc == 2: print(oct(num)[2:])
elif esc == 3: print(hex(num)[2:])