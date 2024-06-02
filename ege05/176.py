def f(n):
    b = bin(n)[2:]
    b = b.replace("1", "2")
    b = b.replace("0", "1")
    b = b.replace("2", "0")
    b = b.replace("0", "1", 1)
    return int(b, 2) + n

for n in range(0, 10000):
    if f(n) < 123:
        print(n)
print(f(13))