import itertools
for i, a in enumerate(itertools.product("елост", repeat=5), 1):
    s = "".join(a)
    if s[0] == "с" and s.count("о") == 2 and "оо" in s:
        print(a)
        print(i)
        break