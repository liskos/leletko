def f(s):
    while "766" in s or "667" in s:
        if "766" in s:
            s = s.replace("766", "67", 1)
        if "667" in s:
            s = s.replace("667", "7", 1)
    return s

r = set()
for n in range(3, 10000):
    s = "7" + n * "6"
    r.add(f(s))
print(len(r))
