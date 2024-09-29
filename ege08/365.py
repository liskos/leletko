import itertools

for i, a in enumerate(itertools.product("ёиклнос", repeat=5), 1):
    s = "".join(a)
    if s.count("ё") >= 2 and s[0] != "о" and s[1] == "к":
        print(i)
        print(s)
