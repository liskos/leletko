import itertools
a = itertools.permutations("просто", r=6) # перемещения
b = set()
for i in a:
    s = "".join(i)
    if "оо" not in s:
        b.add(s)
print(len(b))
        