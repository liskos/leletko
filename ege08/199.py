import itertools
b = 0
for a in itertools.product("abcde", repeat=4):
    s = "".join(a)
    if s.count("a") + s.count("e") == 4:
        if a[0] <= a[1] <= a[2] <= a[3]:
            b += 1
print(b)