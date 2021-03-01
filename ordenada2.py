def ordena(lista):
    
    fim = len(lista)
    for i in range(fim - 1):
        pos_inicial = i
        for j in range(i+1, fim):
            if lista[j] < lista[pos_inicial]:
                pos_inicial = j
                    
        lista[i], lista[pos_inicial] = lista[pos_inicial], lista[i]
    return lista
       






