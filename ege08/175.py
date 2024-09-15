import itertools
b = 0
for a in itertools.product("авикнст", repeat=4):
    s = "".join(a)
    if a[0] in "вкнст" and a[-1] in "аи":
        b += 1
        if s == "ника":
            print(b)
