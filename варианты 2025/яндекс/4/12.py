def k(n):
    return  int(n ** 0.5) ** 2 == n

def s(n):
    n = str(n)
    n = n.replace(">", "0")
    n = int(n)
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

for n in range(1000):
    c = ">" + "0" * 17 + "3" * n + "2" * 17
    d = f(c)
    if k(s(d)):
        print(n)