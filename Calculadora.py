a = float(input("Insira o primeiro valor para calcular: "))
t = int(input
        ("Qual operação deseja fazer ??? \n[1] somar\n[2] multiplicar\n[3] maior número \n[4] novos números\n[5] sair da calculadora\n>>>> "))




b = float(input("Insira o segundo valor: "))
soma = (a + b)


while t != 5:
    if t == 1:
        print(f"O resultado da soma é {soma}")
    t = int(input
        ("Que outra operação deseja fazer ??? \n[1] somar\n[2] multiplicar\n[3] maior número \n[4] novos números\n[5] sair da calculadora\n>>>> "))