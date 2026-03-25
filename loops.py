import random

nro_LANCAMENTOS = int(input("Quantos lacamentos"))
nro_dados = int(input("Quantos dados "))
nro_lados = int(input("Quantos_lados"))

def lancar_dados(lados):
    valor_dado = random.randit(1, lados)
    return valor_dado

def lancar_conjunto_dado(qtde, lados):
    valores_obtido = ""
    for i in range(qtde):
        valores_obtido = f"{valores_obtido} {lancar_dados(lados)}"
    return valores_obtido


