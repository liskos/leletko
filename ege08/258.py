import itertools
b = dict()
for i, a in enumerate(itertools.product("аиклмь", repeat=6), 1):
    b[i] = "".join(a)
print(b)
for i in range(1, len(b)+1 - 26655):
    if b[i] == b[i + 26655][::-1] and b[i][0] == "к" and b[i][-1] == "ь" and len(set(b[i]))==6:
        print(1, i)
