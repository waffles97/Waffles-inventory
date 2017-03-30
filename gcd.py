#Programa hecho por Waffles
def gcd(a, b):
    if a > b:
        small = b
    else:
        small = a
    for c in range(1, small+1):
        if((a % c == 0) and (b % c == 0)):
            gcd = c
    return gcd
################################################################################
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))
gcd = gcd(a, b)
print("The Greatest Common Divisor from ", a," and ", b," is ", gcd)
