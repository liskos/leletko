import itertools
b = 0
for a in itertools.product("антиуопя", repeat=10):
    s = "".join(a)
    if "антиутопия" in s and s[0] == "а" and s[-1] == "я":
        b += 1
print(b)