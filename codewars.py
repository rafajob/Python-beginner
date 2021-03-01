def remove_repetidos(list):
    lista2 = []
    for i in list:
        i[x] = 0
        i[y] = 1
        if i[x] != i[y] :
            lista2.append(i)
            i[x]+1
            i[y]+1
    return lista2
