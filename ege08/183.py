import itertools
b = 0
for a in itertools.permutations("0123456789abcdef", r=15):
    s = "".join(a)
    d = int(s, 15)
    if d[0] >= d[1] > d[2] >= d[3] >= d[4] >= d[5] >= d[6] >= d[7] >= d[8] >= d[9] >= d[10] >= d[11] >= d[12] >= d[13] >= d[14]:
        if s[0] != "0":
            s = s.replace("2", "0")
            s = s.replace("4", "0")
            s = s.replace("6", "0")
            s = s.replace("8", "0")
            s = s.replace("a", "0")
            s = s.replace("c", "0")
            s = s.replace("e", "0")
            s = s.replace("3", "1")
            s = s.replace("5", "1")
            s = s.replace("9", "1")
            s = s.replace("b", "1")
            s = s.replace("d", "1")
            s = s.replace("f", "1")
            if "11" not in s and "00" not in s:
                b += 1
print(b)
