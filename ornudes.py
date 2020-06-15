n = int(input())
a = list(map(int, input().split()))
b=0
for i in range(n):
    if a[n+1] > a[n]:
        b=b+1
print (b)