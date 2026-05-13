kilometros=float(input("Quantos kilometros foram percorrido: "))
dias=float(input("Quantos dias foi alugado: "))

km_rodado=kilometros*0.15

dias_pago=dias*60

gastos=dias_pago+km_rodado

print(f"Nesse total de dias foram gastos {gastos}")