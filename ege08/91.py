import itertools
b = 0
for a in itertools.permutations("калий", r=5):
    s = "".join(a)
    if s[0] != "й" and "иа" not in s:
        b = b + 1
print(b)