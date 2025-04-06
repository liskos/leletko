def f(s:str):
    while "700" in s or "100" in s or "000" in s:
        if "700" in s:
            s = s.replace("700","01", 1)
        if "100" in s:
            s = s.replace("100", "07", 1)
        if "000" in s:
            s = s.replace("000", "1", 1)
    return s

k = 0
for n in range(1000):
    a = "7" + "0" * n
    if f(a).count("7") == 7:
        k = k + n

print(k)