contador = 0

while contador <=5:
    print(f"O Seu contador está em: {contador}")
    contador+=1

print("Fim do loop while")




# Exemplo de CONTINUE: Saltamos o número 3
print("--- Teste do Continue ---")
for i in range(1, 6):
    if i == 3:
        continue # Salta o resto do código deste loop e vai para o próximo número
    print(i)

# Exemplo de BREAK: Paramos o loop assim que encontramos o que queremos
print("--- Teste do Break ---")
for i in range(1, 6):
    if i == 4:
        break # Aborta o loop completamente
    print(i)

    # Forma tradicional:
quadrados_antigo = []
for x in range(1, 6):
    quadrados_antigo.append(x ** 2) # x elevado ao quadrado

# Forma Avançada (List Comprehension):
quadrados_novo = [x ** 2 for x in range(1, 6)]

print(f"Lista gerada: {quadrados_novo}")