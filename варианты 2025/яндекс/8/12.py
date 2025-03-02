def f(n):
    s = str(n)
    while "44" in s or "9299" in s or "49" in s:
        if "49" in s:
            s = s.replace("49","944", 1)
        if "44" in s:
            s = s.replace("44", "2",1)
        if "9299" in s:
            s = s.replace("9299", "4",1)
    return s

v = set()
for n in range(4,1000):
    a = "4" + n * "9"
    v.add(f(a))

print(len(v))

