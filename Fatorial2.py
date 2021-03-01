n = int(input("Digite um númeor inteiro positivo: "))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = (n * fatorial)
        n -= 1
    print(fatorial)
    n = int(input("Digite um númeor inteiro positivo: "))
