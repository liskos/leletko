import itertools
b = 0
for a in itertools.permutations("колун", r=5):
    s = "".join(a)
    s = s.replace("н", "2")
    s = s.replace("л", "2")
    s = s.replace("к", "2")
    s = s.replace("о", "1")
    s = s.replace("у", "1")
    print(s)
    if "22" not in s and "11" not in s:
        b = b + 1
print(b)