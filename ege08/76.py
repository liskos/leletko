import itertools

b = 0
for i, a in enumerate(itertools.permutations("101011010", r=5), 1):
    s = "".join(a)
    if a[0] == "0" and "11" not in s and "00" not in s:
        b = b + 1
print(b)
