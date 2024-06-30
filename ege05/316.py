def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b + b[-3] + b[-2] + b[-1]
    else:
        b = b + str(bin(n % 5 * 5)[2:])
    return int(b, 2)

print(f(12))
print(f(10))
for i in range(5, 1000):
    if f(i) < 100:
        print(i)
