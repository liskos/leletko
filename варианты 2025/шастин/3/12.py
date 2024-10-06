def s(n):
    n = int(n)
    b = 0
    while n > 0:
        b = b + n % 10
        n = n // 10
    return b


def f(s):
    while "411" in s or "1111" in s:
        if "411" in s:
            s = s.replace("411", "14", 1)
        else:
            s = s.replace("1111", "1", 1)
    return s


b = set()
for i in range(3, 10000):
    c = "4" + ("1" * i)
    d = s(f(c))
    b.add(d)
    print(i)
print(max(b))