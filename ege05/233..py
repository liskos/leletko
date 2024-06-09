def f(n):
    b = bin(n)[2:]
    if b.count('1') > b.count('0'):
        b += '0'
    else:
        b += '1'
    m = len(b) // 2
    if len(b) % 2 == 0:
        b = b[:m - 1] + b[m + 1:]
    else:
        b = b[:m - 1] + b[m + 2:]
    return int(b, 2)


a = set()
for i in range(4, 1000):
    if f(i) == 58:
        a.add(i)
print(f(7))
print(len(a))