import itertools
k = 0
for i,a in enumerate(itertools.product("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", repeat=6), 1):
    s = "".join(a)
    if i % 2 == 0:
        k += 1
    if s == "смитап":
        break

print(k)