n=int(input())
s=n
a=1
for i in range(a,n+1):
    if n==0:
        break
    if i%2!=0:
        for j in range(1,s+1):
            print(j,"",end='')
        print("")
    elif i%2==0:
        for d in range(n,a-1,-1):
            print(d,"", end='')
        print("")
    s-=1
    a+=1