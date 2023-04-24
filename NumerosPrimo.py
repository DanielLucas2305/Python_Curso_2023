num = int(input("Insira um valor: "))
cont = 0
for p in range(1, num + 1):
    if num % p == 0:
        print("\033[34m", end = " ")
        cont += 1
    else:
        print("\033[31m", end = "")
    print(p, end = " ")

print(f"\n\033[32mO número {num} foi divisivel por {cont} numeros !")
if cont == 2:
    print("Portanto ele é primo")
else:
    print("Portanto ele NÃO é primo")