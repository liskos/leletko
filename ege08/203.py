import itertools
b = 0
for a in itertools.permutations("10101011", r=5):
    s = "".join(a)
    if "11" not in s and "00" not in s:
        b += 1
print(b)