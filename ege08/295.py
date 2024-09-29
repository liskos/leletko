def f(n):
    n = int(n)
    b = 0
    while n > 0:
        b += n % 10
        n = n // 10
    return b


import itertools
b = 0
for a in itertools.product("012345678", repeat=6):
    s = "".join(a)
    d = s.replace("3","1").replace("5", "1").replace("7", "1")
    if d.count("1") <= 2 and f(s) % 6 == 0 and f(s) % 4 != 0 and s[0] != "0":
        b += 1
        print(s)
print(b)