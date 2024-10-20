def s(n):
    n = int(n)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


def f(s):
    while "002" in s or "22" in s or "222" in s:
        if "002" in s:
            s = s.replace("002", "44", 1)
        else:
            s = s.replace("22", "0", 1)
        if "222" in s:
            s = s.replace("222", "2", 1)
    return s

for i in range(3, 9000):
    b = "0" + "2" * i
    if s(f(b)) == 42:
        print(i, f(b))
