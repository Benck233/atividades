foguete=5

while foguete >0:
    print(f"{foguete}")
    foguete-=1

print("Lançado")

x=[]

for x in range(1,11):
    if x % 2 ==0:
        print(x)


contador=0   

for soma in range(1,5):
    contador+=soma

print(f"o valor final é {contador}")

produtos=["Arroz", "Feijão", "Sabão", "Massa", "Azeite"]

for tamanho in produtos:
    if len(tamanho) == 5:
        print(f"{tamanho}")