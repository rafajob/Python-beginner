def ePrimo(x):
    fator = 2
    while (x > fator):
        teste = x % fator
        if (teste == 0) :
            x -= 1
        fator += 1
    return x
        
def primo_maior(x):
    ePrimo(x)
    return ePrimo(x)
