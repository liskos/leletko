import itertools
k = 0
for i in itertools.product("0123456789abcdef", repeat=5):
    s = "".join(i)
    if s[0] not in "013579bdf" and s[-1] not in "02468ace":
        if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
            k += 1
print(k)