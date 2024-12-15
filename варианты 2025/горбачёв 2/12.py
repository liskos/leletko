def s(n):
    s = 0
    b = int(n)
    while b > 0:
        s = s + b % 10
        b = b // 10
    return s

def f(s):
    s = str(s)
    while "=3" in s or "=4" in s or "=5" in s:
        if "=3" in s:
            s = s.replace("=3", "55=")
        if "=4" in s:
            s = s.replace("=4", "4=")
        if "=5" in s:
            s = s.replace("=5", "3=")
    return s

for i in range(1, 100000):
    d = "=" + 51 * "3" + i * "4" + 53 * "5"
    if len(str(s(f(d)[:-1]))) == 4:
        print(i)