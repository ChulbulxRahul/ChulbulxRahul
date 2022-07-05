def cel(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))


def fah(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))


def temprature():
    i = (input("Enter temperature (ex:67c, 78f): "))
    t = i[-1]
    s = len(i) - 1

    n = i[0:s]
    n = int(n)

    if t == "c":
        cel(n)
    elif t == "f":
       fah(n)
    else:
        print("invalid format")

temprature()