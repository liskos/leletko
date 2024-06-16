def f(n):
    if n % 3 == 0:
        n = n // 3
    else:
        n = n - 1
    if n % 7 == 0:
        n =  n // 7
    else:
        n = n - 1
    if n % 11 == 0:
        n = n // 11
    else:
        n = n - 1
    return n


for i in range(2, 1500):
    if f(i) == 6:
        print(i)
print(f(9))