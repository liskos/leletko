import itertools
b = 0
for a in itertools.product("01234", repeat=6):
    s = "".join(a)
    if s[0] == "3" and int(s) % 2 == 0:
        b += 1
        print(s)
print(b)