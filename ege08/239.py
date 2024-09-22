import itertools
b = set()
for a in itertools.permutations("автомат", r=7):
    s = "".join(a)
    s = s.replace("о", "а")
    s = s.replace("т", "в").replace("м", "в")
    if "аа" not in s and "вв" not in s:
        b.add(a)
        print(a)
print(len(b))