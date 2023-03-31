#programa que soma todos os numeros que são multiplos de 3 num intervalo de 1 a 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0: 
        cont += 1
        soma += soma + c
        print(c, end="; ")

print(f"A soma dos {cont} numeros acima é de {soma}")