def su(n):
    n = int(n)
    s = 0
    while n >0:
        s = s + n%10
        n = n // 10
    return s


def f(n):
    s = str(n)
    while "96" in s or "366" in s or "666" in s:
        if "96" in s:
            s = s.replace("96", "6", 1)
        if "366" in s:
            s = s.replace("366", "69", 1)
        if "666" in s:
            s = s.replace("666", "3", 1)
    return su(s)


r = []
for i in range(3,100):
    a = "9" + "6" * i
    r.append(f(a))

print(max(r))
