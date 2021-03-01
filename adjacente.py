numero = float(input("Digite um numero: "))
teste = 1
teste2 = 0
while (teste != teste2) and (numero != 0) :
     teste = numero % 10
     numero = numero // 10
     teste2 = numero % 10    

if teste == teste2:
     print("Adjacente")
else: 
     print("Não Adjacente")