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