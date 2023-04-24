for p in range(1, 5):
    peso = float(input("Peso da %iª em Kg: " %p))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso


print("O maior peso lido foi de %.2fKg" %maior)
print("O menor peso lido foi de %.2fKg" %menor)