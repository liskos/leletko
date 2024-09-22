import itertools
b = set()
for a in itertools.permutations("ворон", r=5):
    s = "".join(a)
    if "оо" not in s:
        b.add(a)

print(len(b))