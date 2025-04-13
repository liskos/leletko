import itertools
k =0
for a in itertools.permutations("0121212121212", r=5):
    s = "".join(a)
    if s[0] != "0" and "22" not in s and "11" not in s and "02" not in s and "20" not in s:
        k += 1

print(k)