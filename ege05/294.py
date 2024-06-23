def f(n):
    if n % 2 == 0:
        b = sorted(str(n))[::-1]
        b = "".join(b)
        b = int(b) // 2
    else:
        b =  sorted(str(n))
        b = "".join(b)
        b = int(b) * 2
    return b


for i in range(1000,10000):
    if f(i) + 1 == i:
        print(i)
print(f(1488))
print(f(3807))
