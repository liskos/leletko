def f(n):
    s = str(n)
    while "25" in s or "355" in s or "555" in s:
        if "25" in s:
            s = s.replace("25", "5", 1)
        if "355" in s:
            s = s.replace("355", "522", 1)
        if "555" in s:
            s = s.replace("555", "3", 1)
    return s


for i in range(4, 10000):
    v = "2" + "5" * i
    if f(v).count("2") == 10:
        print(i)
        break

