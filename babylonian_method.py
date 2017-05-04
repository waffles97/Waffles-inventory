def babylonian(num):
    x = num/2
    y = 2
    while not (x - y)<0.0001:
        x = (x + y)/2
        y = num/x
    return x

num = float(input("Number: "))
print(babylonian(num))
