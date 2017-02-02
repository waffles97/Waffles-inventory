import math
def minimum_three(x, y, z):
    return min(x,y,z)
def sum_squares(x, y, z):
    return math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)

x = float(input("Dame el primer numero: "))
y = float(input("Dame el segundo numero: "))
z = float(input("Dame el tercer numero: "))
num_min = minimum_three(x, y, z)
num_square = sum_squares(x, y, z)

print("El menor numero de los tres que ingresaste es ", num_min, " y la suma de todos los productos cuadraticos es ", num_square)
