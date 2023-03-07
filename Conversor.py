number = int(input("Escolha um número: "))
print('Escolha uma das bases para a conversão: \n[ 1 ] converter para binario\n[ 2 ] converter para octal\n[ 3 ] converter para hexa')
escolha = int(input("Escolha uma opção: "))
if escolha == 1:
    print("{} convertido para BINÁRIO é igual a ---> {}".format(number, bin(number)[2:]))
elif escolha == 2:
    print("{} convertido para OCTAL é igual a ---> {}".format(number, oct(number)[2:]))
elif escolha == 3:
    print("{} convertido para HEXA é igual a ---> {}".format(number, hex(number)[2:]))
else:
    print("Opção inválida !!!")