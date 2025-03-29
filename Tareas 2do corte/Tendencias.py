import matplotlib.pyplot as plt
import random as r
Y=[]
X=[]
N=int(input("Ingrese la cantidad de numeros aleatorios en el plano: "))
for i in range(N):
    Y.append(r.randint(0,100))
    X.append(r.randint(0,100))
print(f"Los valores de X son {X}")
print(f"Los valores de Y son {Y}")
SX=0
SXY=0
SY=0
SX2=0
for x in range(N):
    SX+=X[x]
    SY+=Y[x]
    SXY+=(Y[x]*X[x])
    D=X[x]**2
    SX2+=D
A=((N*SXY)-(SX*SY))/((N*SX2)-(SX**2))
B=(SY-(A*SX))/N
Xm= min(X)
XM = max(X)
Ym = A * Xm + B
YM = A * XM + B
plt.plot([Xm, XM], [Ym, YM], "b-")
plt.plot(X,Y,"r*")
plt.show()
