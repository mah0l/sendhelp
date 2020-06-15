def task():
    a = input()
    b = input()
    counter = 0
    i = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter


print(task())