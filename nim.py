def computador_escolhe_jogada(n, m):
    if n % (m +1) == 0:
        if m > n:
            n = m
            print()
            print("O computador tirou", n ,"peças")
            print()
            return n
        else:
            m = n - m
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
    print()
    n = int(input("Digite o número de peças a retirar: "))
    print()
    Valido = (n <= m)
    while (Valido == False):
        print("Ops Jogada invalida, tente novamente")
        n = int(input("Digite o número de peças a retirar: "))
        if  (n <= m):
            print("Jogada Valida")
            print("O Jogador retirou", n ,"peças")
            Valido = True
            return n
        else:
            print("O Jogador retirou", n ,"peças")
            return n
    print("O Jogador retirou", n ,"peças")
    return n

def partida():
    vc = 0
    pc = 0
    print()
    n = int(input("Quantas peças? "))
    print()
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
    print("Bem-vindo ao jogo do NIM! Escolha:")
    jogar = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato")
    if (jogar == 1):
                partida()
    else:
        campeonato()
