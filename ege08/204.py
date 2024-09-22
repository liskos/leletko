import itertools
b = 0
for a in itertools.permutations("2101010101", r=6):
    s = "".join(a)
    if "11" not in s and "00" not in s and s[0] != "2" and "20" not in s and "02" not in s:
        b += 1
print(b)