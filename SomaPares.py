soma = 0
cont = 0
for s in range(1, 7):
    numb = int(input(f"Insira o {s}º valor: "))
    if numb % 2 == 0:
        soma += numb
        cont += 1
print(f"Você inseriu {cont} valores pares e a soma deles é igual a {soma}")