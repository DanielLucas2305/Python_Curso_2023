from datetime import date
today = date.today().year
born = int(input("Insira o ano que voce nasceu: "))
idade = today - born

print("O atleta tem %d anos" %(idade))
if idade <= 9:
    print("MIRIM")
elif 9 < idade <= 14:
    print("INFANTIL")
elif 14 < idade <=19:
    print("JUNIOR")
elif 19 < idade <= 21:
    print("SÊNIOR")
else:
    print("MASTER")