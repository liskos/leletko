def su(n:str):
    s = 0
    while len(n) >0:
        s = s + int(n[-1])
        n = n[:-1]
    return s


def f(s:str):
    while "78" in s or "98" in s or "999" in s:
        if "78" in s:
            s = s.replace("78", "8", 1)
        if "98" in s:
            s = s.replace("98", "7", 1)
        if "999" in s:
            s = s.replace("999", "9", 1)
    return s

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            a = "7" * x + "8" * y + "9" * z
            if su(f(a)) == 801:
                print(len(a))
                print(x,y,z)