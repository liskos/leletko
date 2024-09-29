import itertools
b = 0
for a in itertools.product("0101 ", repeat=5):
    s = "".join(a)
    if s[2] == " " and "11" not in s and "00" not in s and s.count(" ") == 1:
        b += 1
        print(s)
print(b)