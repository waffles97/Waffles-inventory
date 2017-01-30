import math
def square_root(x):
    return math.sqrt(x)
def cubic_root(x):
    return math.pow(x, 1/3)

x = float(input("Dame un numero: "))
raiz = square_root(x)
cubica = cubic_root(x)
print("La raiz cuadrada de ", x," es ", raiz, " y la raiz cubica es ", cubica)
