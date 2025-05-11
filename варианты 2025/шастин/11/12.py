def f(s:str):
    while "1" in s:
        if "18" in s:
            s = s.replace("18", "8881", 1)
        else:
            s = s.replace("1", "888", 1)
    return s


a = "1" + "8" * 110
r = f(a)
s = sum([int(x) for x in r])
print(s)
print(r.count("8"))