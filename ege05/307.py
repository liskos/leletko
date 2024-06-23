def f(n):
    c = bin(n)[2:]
    n = n - c.count("0")
    b = bin(n)[2:]
    b = b[-3] + b[-2] + b[-1] + b
    return  int(b, 2)

for i in range(5, 1000):
    if f(i) > 224:
        print(f(i))

print(f(13))