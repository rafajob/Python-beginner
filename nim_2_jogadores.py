def usuario_1_escolhe_jogada(n, m):
    certo = False
    while certo == False: 
        print()
        n = int(input("Digite o número de peças a retirar: "))
        print()
        if n <= m and n > 0:
            print("Jogada Valida")
            print("O Jogador retirou", n ,"peças")
            certo = True
            return n
        else:
            print("Ops Jogada invalida, tente novamente")
    print("O Jogador retirou", n ,"peças")    
    return n

def usuario_2_escolhe_jogada(n, m):
    certo = False
    while certo == False: 
        print()
        n = int(input("Digite o número de peças a retirar: "))
        print()
        if n <= m and n > 0:
            print("Jogada Valida")
            print("O Jogador retirou", n ,"peças")
            certo = True
            return n
        else:
            print("Ops Jogada invalida, tente novamente")
    print("O Jogador retirou", n ,"peças")    
    return n

def main():  
    print()
    print("Bem vindo ao jogo NIM!")
    print()
    j1 = input("Digite o nome para jogador 1: ")
    print()
    j2 = input("Digite o nome para jogador 2: ")
    print()
    print()
    n = int(input("Quantas peças? "))
    while n <= 0:
        n = int(input("Quantas peças? "))
    print()
    m = int(input("Limite de peças por joga? "))
    while m <= 0 and n < m:
        m = int(input("Limite de peças por joga? "))       

    while n != 0:
        if len(j1) > len(j2):
            print()
            print("{} começa".format(j1))
            while n > 0:
                n -= usuario_1_escolhe_jogada(n, m)
                if n == 0:
                    print("{} venceu".format(j1))                    
                else:
                    print("Agora restam", n ,"peças no tabuleiro")
                    n -= usuario_2_escolhe_jogada(n, m)
                    if n == 0:
                        print("{} venceu".format(j2))                        
                    else:
                        print("Agora restam", n ,"peças no tabuleiro")
        else:
            print()
            print("{} começa".format(j2))
            while n > 0:
                n -= usuario_2_escolhe_jogada(n, m)
                if n == 0:
                    print("{} venceu".format(j2))                    
                else:
                    print("Agora restam", n,"peças no tabuleiro")
                    n -= usuario_1_escolhe_jogada(n, m)
                    if n == 0:
                        print("{} venceu".format(j1))
                    else:
                        print("Agora restam", n,"peças no tabuleiro")


main()
    
