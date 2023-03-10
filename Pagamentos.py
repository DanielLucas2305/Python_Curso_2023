print("{:*^52}".format(" DANIEL's SHOP "))
prodprice = float(input("Insira o valor do produto: "))
print("Escolha uma forma de pagamento\n<1> À vista\n<2> À vista no cartão\n<3> 2x no cartão\n<4> 3x ou mais")
option = int(input(":"))


if option == 1:
    vista = (prodprice * 90) / 100
    print("Você pagará R$%.2f reais" %vista)
elif option == 2:
    vista = (prodprice * 95) / 100 ##a variavel pode ser o mesmo nome da de cima###
    print("Você pagará R$%.2f reais" %vista)
elif option == 3:
    print("Você pagará R$%.2f reais" %prodprice)
elif option == 4:
    parce = ((prodprice * 20) / 100) + prodprice
    print("Você pagará R$%.2f reais" %parce)
else:
    print("Opção inválida !!! Tente novamente.")