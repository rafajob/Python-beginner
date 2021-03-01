def menor_nome(nomes):
    pos = 0
    nomes1 = nomes[pos]
    while pos < len(nomes):
        nomes[pos] = nomes[pos].strip()
        if len(nomes[pos]) < len(nomes1):
            nomes1 = nomes[pos]
            
        pos += 1
        
    return nomes1.capitalize()
        
        
