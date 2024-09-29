import itertools
b = set()
for a in itertools.product("компьютер", repeat=5):
    s = "".join(a)
    for f in itertools.product(s, repeat=5):
        d = "".join(f)
        if d == d[::-1]:
            b.add(s)
            print(s)
            break
print(len(b))