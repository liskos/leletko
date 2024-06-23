def f(n):
    b = hex(n)[2:]
    if n % 2 == 0:
        b = b + "f"
    else:
        b = b + "0"
    b = str(b) + hex(sum(int(x, 16) for x in b) % 16)[2:]
    b = str(b) + hex(sum(int(x, 16) for x in b) % 16)[2:]
    c = b.count(max(b))
    d = b.count(min(b)) * 5
    if c == d:
        return int(b, 16)
    else:
        return  b == 0

for i in range(1, 10000000):
    if f(i) > 0:
        print(i)
