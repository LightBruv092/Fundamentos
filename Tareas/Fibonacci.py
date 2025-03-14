n=int(input())
p=0
u=1
i=2
print(p)
print(u)
while i<n+1:
    s=p+u
    p=u
    u=s
    if u<n:
        print(u)
    i=i+1