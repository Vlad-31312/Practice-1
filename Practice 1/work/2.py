a=int(input())
arr=list(map(int,input()))
maxv=0
minv=99999999
for i in range(a):
    ttl=0
    for j in range(a):
        if arr[i]==arr[j]:
            ttl+=1
    if ttl>maxv and arr[i]<minv:
        maxv=ttl
        minv=arr[i]
print(minv)