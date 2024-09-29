import itertools
b = 0
for a in itertools.product("антиуопя", repeat=16):
    s = "".join(a)
    if "антиутопия" in s:
        b += 1
        print(a)
print(b)