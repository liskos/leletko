def f(n):
    s = str(n)
    while "-+" in s or "2++" in s or "++++" in s:
        if "-+" in s:
            s = s.replace("-+", "2+", 1)
        if "2++" in s:
            s = s.replace("2++", "--", 1)
        if "++++" in s:
            s = s.replace("++++", "22", 1)
    return s.count("-") + s.count("+")

for i in range(0,1000):
    n = "-" + ("+" * i)
    if f(n) == 251:
        print(i)