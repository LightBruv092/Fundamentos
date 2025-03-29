N1=int(input())
N2=int(input())
if N1<N2:
    for i in range (1,N1+1,1):
        if N1%i==0 and N2%i==0:
            MCD=i
else:
    if N1>N2:
        i=1
        while i<=N2:
            if N1%i==0 and N2%i==0:
                MCD=i
            i=i+1
    else:
        MCD=N1
print(MCD)