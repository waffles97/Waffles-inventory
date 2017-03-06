# Program made by Waffles
# Main Program
print("Hello, in this program you can convert Fahrenheit to Celsius, isn't that cool???")
tempf = int(input("Give me the temperature in Fahrenheit: "))

tempc = 5*(tempf-32)/9

if tempc>=100:
    print("The temperature in Celsius equals to: ", tempc, ". Also, water can boil at this temperature")
else:
    print("The temperature in Celsius equals to: ", tempc, ". Also, water can't boil at this temperature")
