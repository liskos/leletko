import itertools
b = set()
for a in itertools.permutations("компьютер", r=9):
    s = "".join(a)
    d = s[:4]
    if s[-2] == "е" and s[:4] == "".join(sorted(d)):
        b.add(a)
        print(a)
print(len(b))