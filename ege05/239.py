def sh(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n = n // 6
    return s

def f(n):
    s = sh(n)
    s += s[-1]
    s = int(s, 6)
    s = bin(s)[2:]
    s += s[-1]
    return  int(s, 2)


a = []
for i in range(1, 1000):
    if f(i) < 344:
        a.append(f(i))
print(f(13))
print(max(a))