N=str(input("Ingrese un numero entero positivo: "))
V=""
if int(N)>0:
    B=len(N)
    for i in range(0,B):
        D=int(N[i])+1
        if D==10:
            D=0
        V+=str(D)
    print(V)