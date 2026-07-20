estoque = {
    "Smartphone": {"quantidade": 10, "preco": 800},
    "Notebook": {"quantidade": 5, "preco": 2500},
    "Fone Bluetooth": {"quantidade": 20, "preco": 150}
}

opcoes={"adicionar":1,"remover":2,"ver estoque":3,"sair":4}

numero=1

for opcao, valor in opcoes.items():
    print(f"{numero}. {opcao} = {valor}.")
    numero+=1


while True:
    escolha=input()
    
    if int(escolha) == 4:
        #print(relatorio)
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
        
        if int(escolha) == 4:

            break
