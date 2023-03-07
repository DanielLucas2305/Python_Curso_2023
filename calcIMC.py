peso = float(input("Insira seu peso em KG: "))
high = float(input("Insira sua altura em M: "))
imc = peso / (high ** 2)
print("O seu IMC é igual a %.1f" %(imc))

if imc < 18.5:
    ("ABAIXO DO PESO IDEAL")
elif 18.5 <= imc < 25:
    print("PESO NORMAL")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 <= imc < 40:
    print("OBESIDADE")
elif imc >= 40:
    print("OBESIDADE MÓRBIDA")