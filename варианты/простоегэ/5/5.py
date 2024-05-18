def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b.replace("0", "11")
    else:
        b = b.replace("1", "10")
    return int(b, 2)

for i in range(1, 100):
    if f(i) <= 161:
        print(f(i))
print(f(12))