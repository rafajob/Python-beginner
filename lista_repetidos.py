def remove_repetidos(list):
    lista2 = []
    for i in list:
        if i not in lista2:
            lista2.append(i)
        lista2.sort()
    return lista2
