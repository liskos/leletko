import itertools
b = set()
for a in itertools.permutations("ворота", r=6):
    s = "".join(a)
    s = s.replace("о", "1")
    s = s.replace("а", "1")
    if "11" not in s:
        b.add(a)
print(len(b))