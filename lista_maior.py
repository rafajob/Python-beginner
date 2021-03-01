def maior_elemento(list):
    maior = list[0]
    i = 1
    while i < len(list):
        if list[i] > maior:
            maior = list[i]
        i += 1
        
    return maior
