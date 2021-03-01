import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - (4 * a * c)

if delta < 0:
    print("Esta equação não possui raízes reais")
else:
    x = float((- b + delta)/(2 * a))
    y = float((- b - delta)/(2 * a))
    if (x < y):
        print("As raízes da equação são", x,"e",y)
    else:
        print("As raízes da equação são", y,"e",x)



