# 1= adicionar
#2= remover
#3= olhar etoque
#4= sair e tem q mostrar o relatorio


estoque = {
    "Smartphone": {"quantidade": 10, "preco": 800},
    "Notebook": {"quantidade": 5, "preco": 2500},
    "Fone Bluetooth": {"quantidade": 20, "preco": 150}
}

opcoes={"adicionar":1,"remover":2,"ver estoque":3,"sair":4}

numeros_permitidos=[1,2,3,4]

numero=1


while True:

    for opcao, valor in opcoes.items():
        print(f"{numero}. {opcao} = {valor}.")

        numero+=1

    escolha=input()
    
    if int(escolha) == 4:
        #print(relatorio)
        break

    if int(escolha) ==1:

        print("\n selecine de 1 a 3 para adicionar, caso contrario aperta 4 para sair\n")

        numero_if=1
        for produto, info, in estoque.items():
            print(f"{numero_if}. {produto}, possui {info["quantidade"]} no estoque, e o preço por unidade está em R$ {info["preco"]}.")
            numero_if+=1
        
        print("\n Em qual item você deseja adicionar ?\n")

        escolha=int(input())

        while escolha in numeros_permitidos:

            if int(escolha)==1:
                print(f"Quanto você deseja adicionar ?")

                adicionar_itens=int(input())

                #if adicionar_itens < estoque["Smartphone"]["quantidade"]:
                #    print("Digite um valor maior do que ja existe")
                #    break

                if escolha != adicionar_itens and int(adicionar_itens)>= estoque["Smartphone"]["quantidade"]:
                    estoque["Smartphone"]["quantidade"]+=adicionar_itens
                    print("\nSeu valor foi adicionado")
                    print(f"Novo estoque de Smartphone = {estoque['Smartphone']["quantidade"]}")
                    print("Você deseja continuar adicionando itens ? s/n")
                    opcao_sn =input().lower()
                    if opcao_sn == "n":
                        print("Você voltou ao menu\n")
                        break
                    else:
                        print(f"Novo estoque de Smartphone = {estoque['Smartphone']["quantidade"]}")
                
                else:
                    if int(adicionar_itens)== estoque["Smartphone"]["quantidade"]:
                     
                        estoque["Smartphone"]["quantidade"]=estoque["Smartphone"]["quantidade"]
                        print()

            if int(escolha)==2:
                print(f"Quanto você deseja adicionar ?")

                adicionar_itens=input()

                if escolha != adicionar_itens:
                    estoque["Notebook"]["quantidade"]+= adicionar_itens

                else:
                    estoque["Notebook"]["quantidade"]=estoque["Notebook"]["quantidade"]

            if int(escolha)==3:
                print(f"Quanto você deseja adicionar ?")

                adicionar_itens=input()

                if escolha != adicionar_itens:
                    estoque["Fone Bluetooth"]["quantidade"]+= adicionar_itens
                
                else:
                    estoque["Fone Bluetooth"]["quantidade"]=estoque["Fone Bluetooth"]["quantidade"]

            if int(escolha) == 4:
                print(estoque)
                break



    if int(escolha) == 3:
        numero_if=1
        for produto, info, in estoque.items():
            print(f"{numero_if}. {produto}, possui {info["quantidade"]} no estoque, e o preço por unidade está em R$ {info["preco"]}.")
            numero_if+=1

        escolha=input()

        if int(escolha) == 1:
            
            print(f"{estoque["Smartphone"]}")
        elif int(escolha) ==2:
            print(f"A quantidade de Noebok no estoque é de {estoque['Notebook']["quantidade"]}")
        elif int(escolha) ==3:
            print(f"A quantidade de fone bluethof no estoque é de {estoque['Fone Bluetooth']["quantidade"]}")

        if int(escolha) == 4:

            break


novo_estoque={}