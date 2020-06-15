n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
sum = 0
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            sum += a[i][j]
print(sum)