def ordenada(lista):
    fim = len(lista)
    for i in range(fim):
        pos = i
        if len(lista) != 1:
            for j in range(i + 1, fim):
                if lista[j] < lista[pos]:
                    return False
                else:
                    return True
        else:
            return True






