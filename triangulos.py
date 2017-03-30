#Programa hecho por Waffles
def triangulo(size):
    letra = "T"
    for c in range(size):
        print(letra)
        letra += "T"
    for c in range(1, size):
        letra2 = "T"
        for c in range(size-1-c):
            letra2 += "T"
        print(letra2)
################################################################################
print('Hello, in this program you would be able to make a Triangle made of "T"s')
size = int(input('So lets begin. What is the maximum number of "T"s you want your triangle to be made of?: '))
if size<=0:
    print("The number must be a positive number and must be 1 or higher")
else:
    triangulo(size)
