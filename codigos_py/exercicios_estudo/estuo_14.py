peixe=float(input("Digite o peso do peixe: "))

if peixe>50:
    peixe_multa= (peixe - 50) *4
    print(f"A multa sera de:{peixe_multa}")

else:
    print(f"O peso do peixe é de: {peixe}")

