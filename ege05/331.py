def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = b.replace("1", "2")
        b = b.replace("0", "1")
        b = b.replace("2", "0")
    c = ""
    for i in range(len(b)):
        c = c + b[i] * 2
    return int(c, 2)

print(f(5))
print(f(6))
for i in range(1, 1000):
    if f(i) > 60:
        print(i)