import itertools
b = 0
for i, a in enumerate(itertools.product("аиоуэ", repeat=6),1 ):
    s = "".join(a)
    if s[0] == "о" and s[-1] == "о":
        print(i)

