n, k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(k-1,n-1):
    if a[k-1]!=a[k]:
        break
    k+=1
for k in reversed(range(1, k+1, 1)):
    if a[k-1]!=0:
        break
if a[k-1]==0: k-=1
print(k)