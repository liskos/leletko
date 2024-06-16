def f(n):
    if n % 3 == 0:
        n = n // 3
    else:
        n = n - 1
    if n % 5 == 0:
        n =  n // 5
    else:
        n = n - 1
    if n % 11 == 0:
        n = n // 11
    else:
        n = n - 1
    return n


for i in range(1, 1000):
    if f(i) == 8:
        print(i)
print(f(9))