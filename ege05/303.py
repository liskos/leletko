def p(n):
    r = ""
    while int(n) > 0:
        r = r + str(int(n) % 8)
        n = int(n) // 8
    return r[::-1]
def f(n):
    n = str(n)
    b = ""
    if int(n[0]) % 4 == 0:
        b = "9" + n[1:]
        return str(b)[0], p(b)[-1]
    if int(n[0]) % 2 == 0 and int(n[0]) % 4 != 0:
        b = "3" + n[1:]
        return str(b)[0], p(b)[-1]


a = set()
for i in range(1, 1000):
    if f(i) == ('9', '4'):
        a.add(i)
print(f(41))
print(len(a))