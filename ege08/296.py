def g(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
def f(n):
    n = int(n)
    b = 0
    while n > 0:
        b += n % 10
        n = n // 10
    return b


import itertools
b = 0
for a in itertools.product("0123456", repeat=5):
    s = "".join(a)
    d = s.replace("2","0").replace("4", "0").replace("6", "0")
    if d.count("0") >= 3 and g(f(s)) == True:
        b += 1
        print(s, f(s))
print(b)