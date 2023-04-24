Term1 = int(input("Insira o primeiro termo: "))
raz = int(input("Insira a razão: "))
nt = Term1 + (9 * raz)
print("A sequência dos 10 primeiros termos dessa progressão geométrica é ", end="")
for p in range(Term1, nt+1, raz):
    print(p, end="-> ")
print("FIM !!!")