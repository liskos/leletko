import itertools
b = 0
for a in itertools.permutations("ворон", r=5):
    s = "".join(a)
    if "оо" not in s:
        b = b + 1

print(b)