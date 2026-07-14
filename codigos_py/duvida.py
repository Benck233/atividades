"""
SISTEMA DE MERCADO COM SENTINELA
Sentinela: um valor especial que indica "parar" de adicionar itens
"""

print("=" * 50)
print("BEM-VINDO AO CAIXA DO MERCADO")
print("=" * 50)

# Variáveis para armazenar dados
total = 0
itens = []
sentinela = "0"  # Valor que indica parar de adicionar itens

print("\nDigite os produtos e preços.")
print("Para PARAR, digite 0 (zero) como nome do produto.\n")

# LOOP COM SENTINELA
while True:
    produto = input("Nome do produto (ou 0 para parar): ").strip()
    
    # VERIFICA A SENTINELA
    if produto == sentinela:  # Se for "0", para o loop
        print("\n" + "=" * 50)
        print("FIM DA COMPRA")
        print("=" * 50)
        break
    
    # Se não for sentinela, continua
    try:
        preco = float(input(f"Preço de {produto}: R$ "))
        total += preco
        itens.append({"produto": produto, "preco": preco})
        print(f"✓ {produto} adicionado - Total até agora: R$ {total:.2f}\n")
    except ValueError:
        print("❌ Preço inválido! Digite um número.\n")

# EXIBIR ITENS COMPRADOS
print("\nITENS COMPRADOS:")
for item in itens:
    print(f"  - {item['produto']}: R$ {item['preco']:.2f}")

print(f"\nTOTAL DA COMPRA: R$ {total:.2f}")

# RECEBER PAGAMENTO
pagamento = float(input("\nValor pago: R$ "))

# CALCULAR TROCO
troco = pagamento - total

if troco < 0:
    print(f"❌ Pagamento insuficiente! Faltam R$ {abs(troco):.2f}")
elif troco == 0:
    print(f"✓ Pagamento exato!")
else:
    print(f"✓ Troco: R$ {troco:.2f}")

print("\nObrigado pela compra!")
