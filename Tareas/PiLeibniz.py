N=int(input())
S=0
for i in range (0, N+1, 1):
    S=S+((-1)**i)/(2*i+1)
print(S*4)