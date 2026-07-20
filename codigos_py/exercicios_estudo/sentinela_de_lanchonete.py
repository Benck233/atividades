


menu = {"x-salada":10,"Suco_de_laranja":5,"brigadeiro":8}
conta_total=0
menu_em_lista=list(menu.values())
numero = 1
for item, preco in menu.items():
    print(f"{numero}. {item} = {preco} reais")
    numero = numero + 1  # ou numero += 1

print('Escolha um item do menu, para finalizar seu pedido digite "FIM"')

while True:
    escolha=input()

    if escolha != "FIM" and escolha not in ["1","2","3"]:
        print("Digite um valor valido")
        break

    if str(escolha) == "FIM":
        print(f"O valor da sua conta final foi de: {conta_total}")
        break

    else:

        
        if int(escolha) == 1 :
            conta_total+=menu_em_lista[0]
        elif int(escolha) == 2:
            conta_total+=menu_em_lista[1]
        elif int(escolha) == 3:
            conta_total+=menu_em_lista[2]
        else:
            print("Digite um valor valido")
            break

