def f(n):
    s = sorted(str(n))
    max2 = s[2] + s[1]
    if s[0] != "0":
        min2 = s[0] + s[1]
    elif s[1] != '0':
        min2 = s[1] + s[0]
    else:
        min2 = s[2] + s[0]
    return int(max2) - int(min2)


a = set()
for i in range(900, 1000):
    if f(i) == 70:
        a.add(i)
print(f(351))
print(len(a))