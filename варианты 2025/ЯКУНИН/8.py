import itertools

k =0
for i in itertools.product("012345", repeat=6):
    s = "".join(i)
    if s.count("5") == 0 and s[0] != "0":
        k+=1
print(k)