numeros = []
i = 1
while i != 0: 
    if 0 not in numeros:
        numeros.append(int(input("Digite um número inteiro: ")))
    else:
        i = 0
        del numeros[-1]
        
for numero in numeros[::-1]:
    print(numero)
