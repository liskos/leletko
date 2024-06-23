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

print(f(1488))
print(f(3807))
for i in range(1000,10000):
    if f(i) - 1 == i:
        print(f(i))
        break

