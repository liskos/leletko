import itertools
b = set()
for a in itertools.product("полякв", repeat=4):
    s = "".join(a)
    d = "волк"
    if s[0] == "в":
        if s[1] == "о" or s[2] == "л" or s[3] == "к":
            b.add(s)
    if s[1] == "о":
        if s[2] == "л" or s[3] == "к":
            b.add(s)
    if s[2] == "л":
        if s[3] == "к":
            b.add(s)
print(b)
print(len(b))