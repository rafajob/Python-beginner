def usuario_escolhe_jogada(n, m):
    print()
    n = int(input("Digite o número de peças a retirar: "))
    print()
    Valido = False
    while (Valido == False):
        print("Ops Jogada invalida, tente novamente")
        n = int(input("Digite o número de peças a retirar: "))
        if  (n <= m) and (n > 0):
            print("Jogada Valida")
            print("O Jogador retirou", n ,"peças")
            Valido = True
            return n
        print("O Jogador retirou", n ,"peças")
    return n
