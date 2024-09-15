import itertools

b = 0
for i, a in enumerate(itertools.permutations("1010101010", r=6), 1):
    s = "".join(a)
    if a[0] == "1" and "11" not in s and "00" not in s:
        b = b + 1
print(b)
