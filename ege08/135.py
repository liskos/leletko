import itertools
b = 0
for a in itertools.permutations("кабала", r=6):
    s = "".join(a)
    s = s.replace("а", "1")
    if "11" not in s:
        b = b + 1

print(b)