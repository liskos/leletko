import itertools

b = 0
for i, a in enumerate(itertools.product("ьрплеа", repeat=5), 1):
    s = "".join(a)
    if i > 387:
        break
    if s[-1] == "ь":
        b += 1
        print(i)
print(b)