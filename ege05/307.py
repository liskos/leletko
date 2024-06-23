def f(n):
    c = bin(n)[2:]
    n = n - c.count("0")
    b = bin(n)[2:]
    b = b[-3:] + b
    return int(b, 2)


a = []
for i in range(5, 1000):
    if f(i) > 224:
        a.append(f(i))
print(min(a))

print(f(13))