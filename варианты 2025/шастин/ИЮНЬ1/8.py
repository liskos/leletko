import itertools
k = 0
for i,a in enumerate(itertools.product("абеилртфц", repeat=5), 1):
    s = "".join(a)
    if i % 2 == 1 and s[0] not in "аие" and s.count("ц") == s.count("ф"):
        k += 1

print(k)