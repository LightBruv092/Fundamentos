n=int(input("Ingrese un numero: "))
p=0
u=1
i=2
print(p)
print(u)
if n>2:
    while i<n+1:
        s=p+u
        p=u
        u=s
        if u<n:
            print(u)
        i=i+1
elif n==2:
    print(1)
    print(2)
else:
    print(1)