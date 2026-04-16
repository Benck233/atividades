def desconto(preco, percentual):
    return preco - preco * (percentual /100 )

preco = 100 
percentual = 10 

print(desconto(preco, percentual))

