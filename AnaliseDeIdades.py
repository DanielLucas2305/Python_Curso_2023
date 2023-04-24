from datetime import date
atual = date.today().year
quantmaior = 0
quantmemor = 0
for i in range(1, 8):

    p = int(input(f"Ano de nascimento da {i}ª pessoa: "))
    idade = atual - p

    print(idade, sep=" ")
    if idade >= 18:
        quantmaior += 1
    else:
        quantmemor += 1
print("tivemos %i pessoas maiores" %quantmaior)
print("tivemos %i pessoas menores" %quantmemor)