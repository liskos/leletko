def f(n):
    b = bin(n)[2:]
    if int(str(n)[1]) == b.count("1"):
        n = n + 25
    else:
        n = n - 25
    return n

k = 0
for i in range(100, 201, 2):
    if f(f(i)) == f(i) + 25:
        k += 1
print(k)