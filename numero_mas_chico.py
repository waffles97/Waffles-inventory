#Programa hecho por Waffles
def smallest_of_four(a, b, c, d):
    return min(a, min(b, min(c, d)))
################################################################################
print("Este programa calcula el numero mas chico en una lista de 4 números dados por el usuario")
a = float(input("Introducir primer número: "))
b = float(input("Introducir segundo número: "))
c = float(input("Introducir tercer número: "))
d = float(input("Introducir cuarto número: "))
chico = smallest_of_four(a, b, c, d)
print("El numero más chico es: ", chico)
