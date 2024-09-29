from  itertools import *

a = list(product("01234", repeat=5))

otv = 0
for x in a:
    s = "".join(x)

    flag = 1
    for i in range(1, 5):
        if abs(int(s[i - 1]) - int(s[i])) < 2:
            flag = 0

    if flag == 1 and s[0] != "0":
        otv += 1

print(otv)