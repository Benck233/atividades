# ==============================================================================
# PASSO 1: CRIAÇÃO DA LISTA VAZIA
# Inicializamos uma lista chamada 'quadrados_antigo' sem nenhum elemento dentro.
# ==============================================================================
quadrados_antigo = []

print(f"Lista no início (vazia): {quadrados_antigo}")
print("-" * 40)

# ==============================================================================
# PASSO 2: O LOOP FOR
# O loop vai passar pelos números de 1 até 5 (o 6 é exclusivo).
# A cada volta, a variável 'x' assume o valor do número atual.
# ==============================================================================
for x in range(1, 6):
    
    # PASSO 2.1: Cálculo do quadrado (x elevado a 2)
    resultado_quadrado = x ** 2
    
    # PASSO 2.2: Utilização do .append()
    # Pegamos na lista 'quadrados_antigo' e usamos o .append() para anexar 
    # o 'resultado_quadrado' no final dela.
    quadrados_antigo.append(resultado_quadrado)
    
    # DOCUMENTAÇÃO VISUAL: Mostra o estado da lista a cada volta do loop
    print(f"Volta do loop (x = {x}): Calculou {resultado_quadrado} e adicionou à lista.")
    print(f"Estado atual da lista: {quadrados_antigo}")
    print("-" * 40)

# ==============================================================================
# PASSO 3: EXIBIÇÃO DO RESULTADO FINAL
# Fora do loop, mostramos como a lista ficou preenchida.
# ==============================================================================
print(f"Resultado Final da Lista Gerada: {quadrados_antigo}")