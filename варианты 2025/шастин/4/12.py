def s(n):
    n = int(n, 10)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

def f(s):
    while ">3" in s or ">2" in s or ">0" in s:
        if ">3" in s:
            s = s.replace(">3", "22", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "3>", 1)
        return s

for n in range(1, 10000):
    d = ">" + "0" * 17 + "3" * n + "2" * 17
    print(s(f(d)[3:]) + 3, n)