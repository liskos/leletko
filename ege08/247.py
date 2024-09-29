import itertools

def f(x):
    b = set()
    for a in itertools.product("лог", repeat=x):
        s = "".join(a)
        if "гг" not in s and "оо" not in s and "лл" not in s and s[0] != "г" and s[-1] != "г":
            if "ого" not in s and "лгл" not in s:
                b.add(a)
    return len(b)

a = [0, 0, 0, 0 , 0, 10, 16, 26]

for i in range(13):
    a.append(a[-1] + a[-2])
print(a[-1])
