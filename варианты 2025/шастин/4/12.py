def f(s):
    while (">3" in s) or (">2" in s) or (">0" in s):
        if ">3" in s:
            s = s.replace(">3", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "3>", 1)
    return s[:-1]


for n in range(1, 10):
    d = ">" + "0" * 17 + "3" * n + "2" * 17
    s = sum( int(x) for x in f(d))
    if int(s ** 0.5)**2 == s:
        print(n, s)
        break
