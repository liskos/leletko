import itertools
b = set()
for i, a in enumerate(itertools.product("дейнптья", repeat=5), 1):
    s = "".join(a)
    if s.count("я") == 0 and s.count("е") == 0 and len(s) == len(set(s)):
        print(i)
print(len(b))