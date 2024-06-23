def f(n):
    b = str(n)
    if int(b[0]) % 4 == 0:
        b = "9" + b[1:]
    if int(str(n)[0]) % 2 == 0 and int(str(n)[0]) % 4 != 0:
        b = "3" + b[1:]
    return b


a = set()
for i in range(1000, 10000):
    r = f(i)
    if r and r[0] == "9" and int(r) % 8 == 4:
        a.add(i)
print(len(a))