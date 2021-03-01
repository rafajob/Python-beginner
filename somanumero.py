numero = float(input("Digite um numero: "))
soma = 0
while (numero > 0):
     resto = numero % 10
     numero = numero // 10
     soma += resto
     
print(soma) 