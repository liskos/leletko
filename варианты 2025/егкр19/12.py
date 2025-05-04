def su(n):
    s = 0
    while n >0:
        s = s + n%10
        n = n // 10
    return s

def f(s:str):
    while "42" in s or "8222" in s or "2222" in s:
        if "42" in s:
            s = s.replace("42", "2", 1)
        if "8222" in s:
            s = s.replace("8222", "24", 1)
        if "2222" in s:
            s = s.replace("2222", "8", 1)
    return s

for n in range(3,10000):
    a = "4" + "2" * n
    if su(int(f(a))) == 110:
        print(n)
        break