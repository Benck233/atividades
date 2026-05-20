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


# Se usássemos um dicionário para o resultado:
resultado = {"Notebook": 3500}

print(resultado)


precos=[25.0, 80.0, 12.0, 45.0, 60.0, 8.0]
soma=0
#n_termos=0

for maior in precos:
    soma+=maior
#   n_termos+=1

media=soma/len(precos)

#media=soma/n_termos
media_final=0

for mediana in precos:
    if mediana > media:
        media_final+=1


print(media_final)


"""""
Caso fosse para achar o indice dos preços acima da media


precos = [25.0, 80.0, 12.0, 45.0, 60.0, 8.0]

soma = 0
for preco in precos:
    soma += preco

media = soma / len(precos)  # Média é 38.33

# Criamos uma variável para rastrear a posição atual
indice_atual = 0

print("Índices dos preços acima da média:")

for preco in precos:
    if preco > media:
        # Se for maior, printamos o índice atual em vez de só contar
        print(f"O preço {preco} está no índice: {indice_atual}")
    
    # IMPORTANTE: Avança para o próximo índice a cada elemento da lista
    indice_atual += 1

    """