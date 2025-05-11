import itertools, string
k = 0
for i in itertools.product("0123456789ABCDEFG", repeat=6):
    if len(set(i)) == 6 and i[0] != "0":
        s = "".join(i)
        t = "01"
        sr = ""
        for x in s:
            sr = sr + t[int(x,17)%2]
        if "000" not in sr and "111" not in sr:
            k += 1

print(k)