def f(n):
    b = bin(n)[2:].zfill(8)
    b = b[::-1]
    return n - int(b, 2)

a = []
for i in range(1, 256):
    a.append(f(i))
print(max(a))