n = int(input("Digite um numero inteiro maior que 1: "))

x = 2
m = 0

while (n > 1) :
    while (n % x == 0) :
        m = m + 1
        n = n / x
    if (m > 0) :
        print("Fator = {}, multiplicidade = {}".format(x, m))
    x += 1
    m = 0
