def f(n):
    b = bin(n)[2:]
    c = b + b[-2] + b[1]
    return int(c, 2)


for i in range(2, 100):
    if f(i) > 100:
        print(i)
print(f(11))