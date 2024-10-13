def s(n):
    n = int(n)
    b = 0
    while n > 0:
        b = b + n % 10
        n = n // 10
    return b


def f(s):
    while "96" in s or "6666" in s or "1166" in s:
        if "96" in s:
            s = s.replace("96", "11", 1)
        if "6666" in s:
            s = s.replace("6666", "9", 1)
        if "1166" in s:
            s = s.replace("1166", "69", 1)
    return s


b = set()
for i in range(3, 10000):
    c = "9" + ("6" * i)
    d = s(f(c))
    if d % 37 == 0:
        print(i)