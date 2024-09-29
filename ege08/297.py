from itertools import *

def prime(x):
    if x == 1:
        return 1

    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return 0
    return 1


a = list(product("01234567", repeat=5))

otv = 0
for x in a:
    s = "".join(x)

    flag = 0
    for i in range(5):
        for j in range(i + 1, 5):
            if s[i] != s[j] and prime(int(s[i]) + int(s[j])):
                flag = 1

    if flag == 1 and s[0] != "0":
        otv += 1

print(otv)