import itertools
b = set()
for a in itertools.permutations("ареал", r=5):
    s = "".join(a)
    s = s.replace("а", "1")
    s = s.replace("е", "1")
    if "11" not in s:
        b.add(a)

print(len(b))