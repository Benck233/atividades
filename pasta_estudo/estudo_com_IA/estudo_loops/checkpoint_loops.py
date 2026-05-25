
dicionario_str={"titulo":"Perdido em marte", "autor":"jobson","ano":"2020","paginas":"40" }

for impri in dicionario_str.values():
    print(impri)
print(dicionario_str.get("livros","yablaka"))



estoque = {"arroz": 50, "feijão": 30, "macarrão": 20}

estoque["sal"]=100

estoque["feijão"]=45

del estoque["macarrão"]

produtos = {
    "caneta": {"quantidade": 100, "preco": 2.50},
    "caderno": {"quantidade": 30, "preco": 15.90},
    "borracha": {"quantidade": 75, "preco": 1.20},
}

for produto,dado in produtos.items():
    quantidade=dado["quantidade"]
    preco=dado["preco"]
    total=quantidade*preco
    print(f"Produto: {produto} | Quantidade: {quantidade} | Total: R$ {total}")


#print(produtos)