import itertools

k = 0
for i in itertools.product("донсий", repeat=6):
    s = "".join(i)
    if ("д" in s and "н" not in s) or ("н" in s and "д" not in s):
        if "дд" not in s and "оо" not in s and "нн" not in s and "сс" not in s and "йй" not in s and "ии"  not in s:
            k += 1
print(k)