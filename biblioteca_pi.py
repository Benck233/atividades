import math 

print(math.pi)

import math

print(type(math.pi))           # 3.141592653589793 type(serve para informar que tipo de classe é)
print(math.sqrt(16))     # 4.0
print(math.ceil(2.3))    # 3  (arredonda para cima)
print(math.floor(2.9))   # 2  (arredonda para baixo)
print(math.pow(2, 10))   # 1024.0



import random

print(random.randint(1, 6))    # número inteiro entre 1 e 6
print(random.random())         # número float entre 0.0 e 1.0

nomes = ["Alice", "Bob", "Carol"]
print(random.choice(nomes))    # escolhe um elemento da lista