N=int(input("Ingrese el número: "))
B=int(input("Ingrese la base a convertir: "))
D=2<=B<10
V=""
if N!=0:
    if D==True:
        while N>0:
            R=N%B
            V=str(R)+V
            N//=B
        print(V)
    else:
        print("Base fuera del rango")
else:
    print(0)