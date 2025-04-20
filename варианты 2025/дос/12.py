def su(n):
    s = 0
    while len(n) > 0:
        s = s + int(n[-1])
        n = n[:-1]
    return s


def f(s:str):
    while "31" in s or "211" in s or "1111" in s:
        if "31" in s:
            s = s.replace("31","1",1)
        if "211" in s:
            s = s.replace("211", "13",1)
        if "1111" in s:
            s = s.replace("1111", "2",1)
    return s


for n in range(4,10000):
    a = "3" + "1" * n
    if su(f(a)) == 15:
        print(n)
        break