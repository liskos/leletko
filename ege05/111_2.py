import itertools
def dv(n):
    s = ""
    t = "0123456789ab"
    while n > 0:
        s = t[n%12] + s
        n = n // 12
    return s

def f(s):
    a = int(s[0], 12) + int(s[2], 12)
    b = int(s[1], 12) + int(s[3], 12)
    a, b = sorted([a, b])
    return str(dv(b)) + str(dv(a))

print(f("441b"))

for i in itertools.product("12456b", repeat=4):
    s = "".join(i)
    if f(s) == "115":
        print(s)