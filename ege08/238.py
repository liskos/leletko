import itertools
b = set()
for a in itertools.permutations("веретено", r=8):
    s = "".join(a)
    s = s.replace("о", "е")
    s = s.replace("р", "в").replace("т", "в").replace("н", "в")
    if "ее" not in s and "вв" not in s:
        b.add(a)
        print(a)
print(len(b))
