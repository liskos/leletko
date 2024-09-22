def f(s):
    while "73" in s or "3333" in s or "11330" in s:
        if "73" in s:
            s = s.replace("73", "11", 1)
        if "3333" in s:
            s = s.replace("3333", "7", 1)
        if "1133" in s:
            s = s.replace("1133", "37", 1)
    return s


for n in reversed(range(4, 10000)):
    s = "7" + n * "3"
    if sum(map(int, f(s))) == 128:
        print(n)
        break
    if n % 100 == 0:
        print(n//100, "%", n)
