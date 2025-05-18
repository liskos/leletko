def f(s:str):
    while "444" in s or "777" in s:
        if "777" in s:
            s = s.replace("777", "4", 1)
        else:
            s = s.replace("444", "7", 1)
    return s

r = []
for n in range(4,1000):
    a = "4" + "7" * n
    r.append(sum([int(x) for x in f(a)]))

print(max(r))
