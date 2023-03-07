from datetime import date
today = date.today().year
nasc = int(input("Ano que voce nasceu: "))
idade = today - nasc
print ("Quem nasceu em {} tem {} anos de idade.".format(nasc, idade))

if idade == 18:
    print("Voçe deve se alistar esse ano")
elif idade < 18:
    tempo = 18 - idade
    tempo_rest = today + tempo
    print ("faltam {} anos para voce se alistar".format(tempo))
    print("Seu alistamento será em %d" %(tempo_rest))
elif idade > 18:
    tempo_passado = idade - 18
    tempo_rest = today - tempo_passado
    print("Voce deveria se alistar a %d anos atras !!!" %(tempo_passado))
    print("Seu alistamento foi em %d" %(tempo_rest))