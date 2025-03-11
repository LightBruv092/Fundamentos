N=int(input("Ingrese el número: "))
B=int(input("Ingrese la base a convertir entre 2,4,8 o 16: "))
D=B==2 or B==4 or B==8 or B==16
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