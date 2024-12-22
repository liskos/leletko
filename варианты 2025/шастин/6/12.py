def s(n):
    n = int(n)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


def f(s):
    s = str(s)
    while ">3" in s or ">5" in s or ">7" in s:
        if ">3" in s:
            s = s.replace(">3", "55>", 1)
        if ">5" in s:
            s = s.replace(">5", "5>3", 1)
        if ">7" in s:
            s = s.replace(">7", "3>5", 1)
    return s

print(s(f(">" + 10 * "3" + 10 * "5" + 10 * "7")[:-1]))