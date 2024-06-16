def f(n):
    b = bin(n)[2:]
    b = b[1:]
    b = b.replace("0", "2")
    b = b.replace("1", "0")
    b = b.replace("2", "1")
    return n + int(b, 2)

for i in range(3, 1000):
    if f(i) > 99:
        print(i)
print(f(5))