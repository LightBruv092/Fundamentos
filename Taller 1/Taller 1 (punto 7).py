N=int(input("Ingrese un número: "))
MC=0
PC=0
MA=0
PA=0
while N!=0:
    if N>0:
        print("Es positivo")
        PA+=N
        PC+=1
    elif N<0:
        print("Es negativo")
        MA += N
        MC += 1
    N = int(input("Ingrese un número: "))
if N==0:
     print("Es cero")
PP=PA/PC
PM=MA/MC
print("Hubieron",PC,"números positivos","con",PP,"como promedio")
print("Hubieron",MC,"números negativos","con",PM,"como promedio")