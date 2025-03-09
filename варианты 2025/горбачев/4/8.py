import itertools

k = 0
for i in itertools.product("0123456", repeat=7):
    s = "".join(i)
    if s[0] not in "035" and s[-1] not in "0246" and s.count("0") <= 1:
        k += 1

print(k)