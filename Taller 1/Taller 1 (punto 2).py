N=int(input("Ingrese un número entero mayor que 2: "))
while N<=2:
    print("Tiene que ser un entero mayor a 2")
    N = int(input("Ingrese un número entero mayor que 2: "))
for i in range(N,0,-1):
    C=0
    for x in range(1, N+1):
        if i % x == 0:
            C+=1
    if C==2:
        P=i
        break
print(P)