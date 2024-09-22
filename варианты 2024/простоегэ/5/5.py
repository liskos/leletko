def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b.replace("0", "11")
    else:
        b = b.replace("1", "10")
    return int(b, 2)

a = []
for i in range(1, 1000):
    if f(i) <= 161:
        a.append(f(i))
print(max(a))