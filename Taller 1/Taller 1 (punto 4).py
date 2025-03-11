N=int(input("Digite un número: "))
D=int(input("Digite otro número: "))
C=N*D
if N<D:
    for i in range (1,N+1,1):
        if N%i==0 and D%i==0:
            MCD=i
else:
    if N>D:
        i=1
        while i<=D:
            if N%i==0 and D%i==0:
                MCD=i
            i=i+1
    else:
        MCD=N

if N%2==0 and D%2==0:
    print(MCD)
elif N%2==1 and D%2==1:
    print (MCD)
else:
    R=C/MCD
    print(R)