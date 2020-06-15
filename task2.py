a = list(map(int, input().split()))


def booleans(a, b, c):

    if a + b + c <= 1:
        return 'false'
    else:
        return'true'

print(booleans(a[0], a[1], a[2]))