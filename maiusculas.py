def maiusculas(frase):
    pos = 0
    string1 = ""
    teste = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
             76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
             86, 87, 88, 89, 90]
    while pos < len(frase):
        if ord(frase[pos]) in teste:
            string1 = string1 + frase[pos]
        pos = pos + 1
    return string1



