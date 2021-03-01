numero = float(input("Digite um numero: "))
x = 2

primo = True

while (numero > x) and primo:
     teste = numero % x
     if (teste == 0) :
         primo = False
     x += 1
if primo:
     print("Primo")
else: 
     print("Não primo")