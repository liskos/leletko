import itertools
b = set()
for a in itertools.permutations("аттестат", r=8):
    s = "".join(a)
    s = s.replace("а", "е")
    s = s.replace("с", "т")
    if "ее" not in s and "тт" not in s:
        b.add(a)
        print(a)
print(len(b))