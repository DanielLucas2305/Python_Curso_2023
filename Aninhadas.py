nome = str(input("Qual é o seu nome ??? "))
if nome == 'Daniel':
    print ("Que nome bonito!!!")
elif nome == "Pedro" or nome == "Maria" or nome =="Ana":
    print ("Seu nome é bem normal no Brasi")

#in significa dentro das aspassdsdedcfw
elif nome in "Claudia Jessica Juliana":
    print("Belo nome feminino")
else:
    print ("Seu nome é bem normal")
print("Tenha um bom dia {}" .format(nome))