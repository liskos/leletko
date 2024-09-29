import itertools
b = set()
for a in itertools.permutations("препарат", r=8):
    s = "".join(a)
    s = s.replace("е", "а")
    s = s.replace("п", "р").replace("т", "р")
    if "аа" in s or "рр" in s:
        b.add(a)
        print(a)
print(len(b))