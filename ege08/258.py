import itertools
b = set()
for i, a in enumerate(itertools.product("аиклмь", repeat=6), 1):
    s = "".join(a)
    b.add(i,s)
    if s[0] == "к" and abs(i - d) == 26655:
        print(i)
