def computador_escolhe_jogada(n, m):
    if n % (m +1) == 0:
            n = m
            print()
            print("O computador tirou", n ,"peças")
            print()
            return n       
    else: 
        n = n % (m + 1)
        print()
        print("O computador tirou", n ,"peças")
        print()
        return n
       
    
def usuario_escolhe_jogada(n, m):
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

def partida():
    print()
    n = int(input("Quantas peças? "))
    while n <= 0:
        n = int(input("Quantas peças? "))
    print()
    m = int(input("Limite de peças por joga? "))
    while m <= 0 and n < m:
        m = int(input("Limite de peças por joga? "))       

    while n != 0:
        if (n % (m + 1)) == 0:
            print("Você começa")
            while n > 0:
                n -= usuario_escolhe_jogada(n, m)
                if n == 0:
                    print("Usuario venceu")                    
                else:
                    print("Agora restam", n ,"peças no tabuleiro")
                    n -= computador_escolhe_jogada(n, m)
                    if n == 0:
                        print("Computador venceu")                        
                    else:
                        print("Agora restam", n ,"peças no tabuleiro")
        else:
            print("Computador começa")
            while n > 0:
                n -= computador_escolhe_jogada(n, m)
                if n == 0:
                    print("Computador venceu")                    
                else:
                    print("Agora restam", n,"peças no tabuleiro")
                    n -= usuario_escolhe_jogada(n, m)
                    if n == 0:
                        print("Usuario venceu")
                    else:
                        print("Agora restam", n,"peças no tabuleiro")
    

def campeonato():
    rodada = 1
    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        partida()
        rodada += 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")

def main():
    print()
    print("Bem-vindo ao jogo de NIM! Escolha:")
    print()
    j = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    if j == 1:
            print()
            print(" Você escolheu partida isolada!")
            partida()
    else:
        print()
        print("Você escolheu campeonato!")
        campeonato()

main()
