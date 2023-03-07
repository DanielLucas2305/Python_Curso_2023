note1 = float(input("Insira a primeira nota: "))
note2 = float(input("Insira a segunda nota "))

#formula da media

media = (note1 + note2) / 2

print ("A sua média é igual a {}" .format(media))

if media < 5:
    print("Reprovado")
elif media <= 6.9999:
    print("recuperação !")
elif media >=7:
    print("Aprovado")