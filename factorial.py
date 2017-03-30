#Programa hecho por Waffles
################################################################################
def factorial(num):
    n = 1
    while n>=1:
        n *= num
        num -= 1
    return n
    print()
################################################################################
num = int(input("Numero al que sacarle factorial (solo se pueden recibir numeros enteros): "))
factorial(num)
