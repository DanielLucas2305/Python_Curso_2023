frase = str(input("Insira a frase: ")).strip().upper()#strip tira os espaços e upper deixa todas maiusculas 
words = frase.split()#split separa as palavras
too = "".join(words)#junta todas as palavras com a condição definida em """
inver = ''

for l in range(len(too) -1, -1, -1): #vai da ultima até a primeira(menos uma pois o ultimo não conta), ao contrário
        inver += too[l] 
    
print(f"A frase junta é {too} e o inverso é '{inver}'")

if inver == too:
    print("É um palíndromo")
else:
    print("Não é um palíndromo !")
