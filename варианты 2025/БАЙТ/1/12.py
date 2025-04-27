def su(n:str):
    s = 0
    while len(n) > 0:
        s = s + int(n[-1])
        n = n[:-1]
    return s

def f(s:str):
    while "211" in s or "1111" in s or "411" in s:
        if "211" in s:
            s = s.replace("211", "14",1)
        if "1111" in s:
            s = s.replace("1111", "11",1)
        if "411" in s:
            s = s.replace("411", "12", 1)
    return s

r = []
for n in range(3,10000):
    a = "2" + "1" * n
    if su(f(a)) % 2 == 0:
        r.append(n)

print(max(r))