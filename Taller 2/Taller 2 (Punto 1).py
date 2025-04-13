A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#lista de el abecedario
def c1(B,A):
    V=len(B)
    C=B
    for i in range(0,V,2):
        D=A.index(B[i])
        C=C[:i]+A[D+3]+C[i+1:]
    return C
#funcion que cambia las letras pares por la letra 3 posiciones adelante
def c2(S,A):
    V = len(S)
    F = S
    for i in range(1, V, 2):
        D = A.index(S[i])
        F = F[:i] + A[D + 4] + F[i + 1:]
    return F
#funcion que cambia las letras impares por la letra 4 posiciones adelante
G=str(input("Ingrese la palabra: "))
B=G.lower()
#funcion que pone el texto en minúscula, a razón de que en la lista inicial no hay mayúsculas
S=c1(B,A)
H=c2(S,A)
print(H)