print("{:*^52}".format(" DANIEL's SHOP "))
prodprice = float(input("Insira o valor do produto: "))
print("Escolha uma forma de pagamento\n<1> À vista(10% de desconto)\n<2> À vista no cartão(5% de desconto)\n<3> 2x no cartão\n<4> 3x ou mais(20% de juros)")
option = int(input(":"))


if option == 1:
    vista = (prodprice * 90) / 100
    print("Você pagará R$%.2f reais" %vista)
elif option == 2:
    vista = (prodprice * 95) / 100 ##a variavel pode ser o mesmo nome da de cima###
    print("Você pagará R$%.2f reais" %vista)
elif option == 3:
    parce = prodprice / 2
    print("Você pagará 2 parcelas de R$%.2f reais" %parce)
elif option == 4:
    vezes = int(input("Quantas vezes deseja parcelar ? "))
    parce = (prodprice + (prodprice * 20 / 100)) / vezes
    print("Você pagará %i parcelas de R$%.2f reais" %(vezes, parce))
else:
    print("Opção inválida !!! Tente novamente.")


#teste commit git#