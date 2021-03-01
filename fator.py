n = int(input("Digite o valor de n: "))
fator = 1

while n > 0:
    fator = fator * n
    n -= 1
    if fator == 0:
        fator = 1

print(fator)