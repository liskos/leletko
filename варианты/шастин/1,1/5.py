def s(n):
    a = 0
    while int(n) > 0:
        a = a + int(n) % 10
        n = int(n) // 10
    return a

def f(n):
    b = bin(n)[2:]
    if s(b) % 2 == 0:
        b = b + "11"
    else:
        b = b + "01"
    return int(b, 2)

print(f(4))
print(f(5))
for i in range(1, 1000):
    if f(i) > 61:
        print(f(i))
        break