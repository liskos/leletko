import itertools
b = 0
for a in itertools.product("0123456789", repeat=6):
    s = "".join(a)
    d = s
    if d[0] != 0 and d[0] > d[1] > d[2] > d[3] > d[4] > d[5]:
        s = s.replace("2", "0")
        s = s.replace("4", "0")
        s = s.replace("6", "0")
        s = s.replace("8", "0")
        s = s.replace("3", "1")
        s = s.replace("5", "1")
        s = s.replace("9", "1")
        if "11" not in s and "00" not in s:
            b += 1
print(b)
