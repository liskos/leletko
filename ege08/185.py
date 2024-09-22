import itertools
b = 0
for a in itertools.product("0123456789", repeat=6):
    s = "".join(a)
    if a[0] != 0 and a[0] > a[1] > a[2] > a[3] > a[4] > a[5]:
        for i in range(10):
            s = s.replace(str(i), str(i % 2))
        if "11" not in s and "00" not in s:
            b += 1
print(b)
