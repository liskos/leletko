import itertools
b = 0
for a in itertools.permutations("01234567", r=5):
    s = "".join(a)
    if s[0] != "0":
        s = s.replace("2", "0")
        s = s.replace("4", "0")
        s = s.replace("6", "0")
        s = s.replace("3", "1")
        s = s.replace("5", "1")
        s = s.replace("7", "1")
        if "11" not in s and "00" not in s:
            b += 1
print(b)

