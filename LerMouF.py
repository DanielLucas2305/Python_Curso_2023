r = "M" or "F"
while r == "M" or r == "F":
    r = str(input("Digite o sexo [M/F]: ")).upper()
    if r != "M":
        if r != "F":
            print("Digite M ou F !!!")