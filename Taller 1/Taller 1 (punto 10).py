n=int(input("Ingrese un numero: "))
p=0
u=1
i=2
if n>2:
    while i<n+1:
        s=p+u
        p=u
        u=s
        if u>n:
            print(u)
            break
elif n==2:
    print(3)
else:
    print(1)