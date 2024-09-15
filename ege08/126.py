import itertools

for i, a in enumerate(itertools.product("уоа", repeat=5), 1):
    if i == 100:
        print(a)
        break
