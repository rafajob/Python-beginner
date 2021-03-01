def soma_matrizes(m1, m2):
    x1 = len(m1)
    y1 = len(m1[0])
    x2 = len(m2)
    y2 = len(m2[0])
    m3 = []
    if x1 == x2 and y1 == y2:
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2 [i][j])
            m3.append(linha)
        return m3
    else:
        return False



    
