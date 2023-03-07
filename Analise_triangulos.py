are1 = float(input("Primeira aresta: "))
are2 = float(input("Segunda aresta: "))
are3 = float(input("Terceira aresta: "))

if are1 < are2 + are3 and are2 < are1 + are3 and are3:
    print('Os segmentos inseridos podem formar um triângulo ', end="")
    if are1 == are2 == are3:
        print("EQUILÁTERO")
    if are1 != are2 != are3 != are1:
        print("ESCALENO")
        ###ou apenas um "else"
    if are1 == are2 or are1 == are3 or are2 == are3:
        print("ISÓSECELES")
else:
    print("Os segmentos NÃO podem formar um triangulo !!!")