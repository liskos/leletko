def f(n):
    b = bin(n)[2:]
    if n % 4 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = str(bin(n % 4 * 2)[2:]) + b
    return int(b, 2)

print(f(12))
print(f(10))
for i in range(5, 1000):
    if f(i) < 68:
        print(i)
