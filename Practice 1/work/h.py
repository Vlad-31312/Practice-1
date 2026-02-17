a=int(input())
count=0
x=0
maxv=-99999999
arr=list(map(int,input().split()))
for i in range(a):
    count=0

    for j in range(a):
        if arr[i]==arr[j]:
            count+=1
        if count>max:
              maxv=count
               x=arr[i]
print(max)