import itertools
b = set()
for a in itertools.permutations("тикток", r=6):
    s = "".join(a)
    if "кк" not in s and "тт" not in s:
        b.add(s)
        print(s)
print(len(b))