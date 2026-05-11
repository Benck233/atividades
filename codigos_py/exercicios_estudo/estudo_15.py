ganho=float(input("Quanto você ganha por hora: "))
horas=float(input("Quanto horas você trabalha no mês: "))

salario_bruto= ganho*horas

desconto_impostoR=salario_bruto * (11/100)

desconto_inss=salario_bruto * (8/100)

desconto_sindicato=salario_bruto*(5/100)

salario_liquido=salario_bruto-desconto_sindicato-desconto_inss-desconto_impostoR

print(f"Seu salario bruto é: {salario_bruto}")
print(f"Você pagou ao Imposto de renda: {desconto_impostoR}")
print(f"Você pagou para o inss: {desconto_inss}")
print(f"Você pagou para o sindicato: {desconto_sindicato}")
print(f"O seu salario liquido é de: {salario_liquido}")