import  itertools

b = 0
for a in itertools.product("1234567", repeat=9):
    s = "".join(a)
    if "11" not in s and "22" not in s and "33" not in s and "44" not in s and "55" not in s and "66" not in s and "77" not in s:
        b += 1
print(b)
print(252 + 1512 + 9072 + 54432 + 326592 + 1959552 + 11757312)