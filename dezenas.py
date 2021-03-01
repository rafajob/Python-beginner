inteiro_str = input("Digite um número inteiro: ")
inteiro = int(inteiro_str)

dezena = inteiro // 10
dezena_final = dezena % 10
print("O dígito das dezenas é" ,dezena_final)