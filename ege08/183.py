import itertools
b = 0
for a in itertools.permutations("0123456789abcdef", r=15):
    s = "".join(a)
    d = int(s, 15)

            if "11" not in s and "00" not in s:
                b += 1
print(b)
