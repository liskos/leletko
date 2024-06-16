def f(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = n - 1
    if n % 5 == 0:
        n =  n // 5
    else:
        n = n - 1
    if n % 7 == 0:
        n = n // 7
    else:
        n = n - 1
    return n


for i in range(1, 1000):
    if f(i) == 6:
        print(i)
print(f(9))