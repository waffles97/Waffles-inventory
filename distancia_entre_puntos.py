#Programa hecho por Waffles
import math
################################################################################
def distancia_entre_puntos(x1, y1, x2, y2):
    dist = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    return dist
################################################################################
print("Este programa calcula la distancia entre dos puntos en el eje X y el eje Y")
x1 = float(input("Ingrese el valor de x1: "))
y1 = float(input("Ingrese el valor de y1: "))
x2 = float(input("Ingrese el valor de x2: "))
y2 = float(input("Ingrese el valor de y2: "))
distancia_entre_puntos = distancia_entre_puntos(x1, y1, x2, y2)
print("La distancia entre los dos puntos es de: ", distancia_entre_puntos)
