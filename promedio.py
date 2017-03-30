#programa hecho por waffles
def promedio_lista(num):
    a = [None] * num
    for i in range(num):
        numero = int(input("Ingresar el numero: "))
        a[i] = numero
    print("El promedio de ", a, " es de: ", sum(a)/len(a))
################################################################################
print("Este programa calcula el promedio de ciertos números dados por el usuario")
num = int(input("Cuántos números desea ingresar?: "))
promedio_lista = promedio_lista(num)
print(promedio_lista)
