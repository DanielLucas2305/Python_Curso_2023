number = int(input("Insira um número para mostrarmos a tabuada: "))
for t in range(1, 11):
    tab = t * number
    print(f"{t} X {number} = {tab}", end="\n")