N=int(input("Ingrese el limite máximo: "))
if N>2:
    for i in range(2,N+1,1):
        if i%2==0 or i%3==0 or i%5==0:
            print(i)
elif N==2:
    print(2)
else:
    print("Valor invalido")