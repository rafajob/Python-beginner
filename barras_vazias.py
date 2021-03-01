x = int(input("digite a largura: "))
y = int(input("digite a altura: "))
l = x
a = y - 1

while y > 0:
    s = (x - 4)*" "
    print(x*"#", end = "\n")
    while y > 1:
        if a < y and y > 2:
            print("#",s,"#" ,end = "\n")
            a -= 1
        else:
            print(x*"#", end = "\n")
        y -= 1
    y -= 1
    
