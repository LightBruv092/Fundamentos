def L(C):
    d = ""
    for i in C:
        if i not in d:
            d += i
    return d
F=""
def P(S,F=""):
    if len(S)==0:
        print(F)
    else:
        for i in  range(len(S)):
            G=S[i]
            R=S[:i]+S[i+1:]
            P(R,F+G)
N=str(input("Ingrese una secuencia de letras: "))
S=L(N)
A=P(S,F)
