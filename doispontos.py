import math

x1 = int(input("Digite x1: "))
y1 = int(input("Digite y1: "))
x2 = int(input("Digite x2: "))
y2 = int(input("Digite y2: "))

d = ((x1 - x2)**2) + ((y1 - y2)**2)

if d < 0:
    print("Raiz Negativa")
else: 
    raiz = math.sqrt(d)
    if raiz >= 10:
        print("Longe")
    else:
        print("Perto")
        