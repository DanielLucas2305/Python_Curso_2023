from random import randint
itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)
print("Suas jogadas:\n<0> Pedra\n<2> Papel\n<3> Tesoura")
player = int(input("Sua opção: "))
print("-*" * 10)
print("Jogador jogou {}".format(itens[player]))
print("Computador jogou {}".format(itens[pc]))
print("-*" * 10)

if pc == 0:
    if player == 0:
        print("EMPATE!!!")
    elif player == 1:
        print("JOGADOR GANHOU")
    elif player == 2:
        print("COMPUTADOR GANHOU!!!")
    else:
         print("JOGADA INVÁLIDA")
elif pc == 1:
    if player == 0:
        print("COMPUTADOR GANHOU!!!")
    elif player == 1:
        print("EMPATE!!!")
    elif player == 2:
        print("JOGADOR GANHOU")
    else:
        print("JOGADA INVÁLIDA")
elif pc == 2:
    if player == 1:
        print("COMPUTADOR GANHOU!!!")
    elif player == 0:
        print("JOGADOR GANHOU")
    elif player == 2:
        print("EMPATE!!!")
    else:
        print("JOGADA INVÁLIDA")


#Está com algum erro que não foi revisado