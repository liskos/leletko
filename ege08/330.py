import itertools
b = set()
for a in itertools.permutations("водопад", r=7):
    s = "".join(a)
    if "оо" not in s and "аа" not in s and "оа" not in s and "ао" not in s:
        b.add(s)
        print(s)
print(len(b))