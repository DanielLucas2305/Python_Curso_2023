r = "M" or "F"
while r != "M" or r != "F":
    r = str(input("Digite o sexo [M/F]: ")).upper()
    if r != "M" or r != "F":
        print("Digite M ou F !!!")
        # if r != "F":
        #     print("Digite M ou F !!!")    #pode ser feito dessa maneira, porem com mais linhas