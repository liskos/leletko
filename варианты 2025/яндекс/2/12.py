def f(n):
    if "52" in s or "2222" in s or "1112" in s:
        if "52" in s:
            s.replace("52", "11", 1)
            s.replace("2222", "5", 1)
        else:
            s.replace("1112", "2", 1)
    return s

for i in range(4, 10000):
    s = "5" + "2" * i
    d = f(s).count("1") + f(s).count("2") * 2 + f(s).count("5") * 5
    if d == 1685:
        print(i)