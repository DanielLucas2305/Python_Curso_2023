contI = 0
idahom = 0
nomehom = ''
contMul = 0

for n in range(1, 5):
    print('\033[33m' + (f'--------{n}ª PESSOA--------')+'\033[0;0m')
    nome = str(input("Insira o nome da %iª pessoa: " %n))
    sexo = str(input("Insira o sexo da %iª pessoa[M / F]: " %n)).upper()
    print(sexo)
    idade = int(input("Insira a idade da %iª pessoa: " %n))
    contI += idade
    if n == 1 and sexo == "M":
        idahom = idade
        nomehom = nome
    if sexo == "M" and idade > idahom:
        idahom = idade
        nomehom = nome
    if sexo == "F" and idade < 20:
        contMul += 1
    
if contMul == 1:
    m = str("mulher")
else:
    m = str("mulheres")
med = contI / 4
print("A média de idade é de %i anos." %med)
print(f'O homem mais velho é {nomehom} com {idahom} anos de vida !')
print("Ao todo foram %i %s abaixo de 20 anos" %(contMul, m))
#print("A pessoa mais velha tem %i anos e a mais nova tem %i" %(maisv, menosv))