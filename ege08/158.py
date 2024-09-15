import itertools
b = 0
for a in itertools.permutations("0123456789", r=7):
    s = "".join(a)
    if s[0] != "0" and int(s) % 5 == 0:
        s = s.replace("2", "0")
        s = s.replace("4", "0")
        s = s.replace("6", "0")
        s = s.replace("8", "0")
        s = s.replace("3", "1")
        s = s.replace("5", "1")
        s = s.replace("7", "1")
        s = s.replace("9", "1")
        if "11" not in s and "00" not in s:
            b += 1
print(b)

