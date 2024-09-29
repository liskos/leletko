import itertools

b = 0
for a in itertools.permutations("Х1Ч1Н1Б1ДЖ1Т", r=12):
    s = "".join(a)
    if "11111" in s:
        b += 1
        print(s)
print(b)