def calcula_area_quadrado(lado):
    print(f"a area do {lado} é {lado * lado} ")
    area = lado * lado


    print(f"a area do {lado} é {area} ")

calcula_area_quadrado(6)

def calcula_area_triangolo(base, altura):
    area = base * altura /2 
    print(f"a area do triangulo é {area}")
    return area


def imprime_area(figura, valor):
    print(f"a area do {figura} é {valor} ")


area = calcula_area_triangolo(2, 3 )
    