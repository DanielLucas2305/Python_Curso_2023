#Operações

valor_casa = float(input("Insira o valor da casa: "))
salario = float(input("Insira sua renda mensal: "))
anos = int (input("Em quantos anos voce quer pagar? "))

prestacoes = valor_casa / (anos * 12)
pct_salario = salario / 100 * 30

#condicoes
if prestacoes > pct_salario:
    print ("Infelizmente não será possível a liberação do crédito")
    print ("Voce pagaria prestaçoes de {}" .format(prestacoes))
else:
    print ("Otimo, vc pagara parcelas de {} reais" .format(prestacoes))