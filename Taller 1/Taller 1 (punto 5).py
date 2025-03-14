N=int(input("Ingrese el número: "))
B=N
i=2
while i<16:
    N=B
    V = ""
    if N!=0:
        while N>0:
            R=N%i
            V=str(R)+V
            N//=i
        print(V)
    else:
        print(0)
    i*=2
N=B
F=""
T="ABCDEF"
while N>0:
    H=N%i
    T="ABCDEF"
    if H>9:
        X=H-10
        F=str(T[X])+F
    else:
        F=str(H)+F
    N//=i
N=B
if N!=0:
    print(F)
else:
    print(0)