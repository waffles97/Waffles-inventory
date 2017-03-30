#programa hecho por Waffles
import math
################################################################################
def sumsquares_list(a, b, c, d, e):
    return math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2) + math.pow(d, 2) + math.pow(e, 2)
################################################################################
print("Este programa calcula la suma de 5 numeros dados por el usuario, elevados al cuadrado.")
a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))
c = float(input("Introduce el tercer numero: "))
d = float(input("Introduce el cuarto numero: "))
e = float(input("Introduce el quinto numero: "))
suma = sumsquares_list(a, b, c, d, e)
print("La suma total es de: ", suma)
