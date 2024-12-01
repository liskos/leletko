r = set()

for x in range(1, 25):
    v = "0123456789ABCDEFGHIJKLMNO"
    a = "8af7" + v[x] + "11"
    b = v[x] + "da87"
    for d in range(1, 101):
        if (int(a, 25) + int(b, 25)) % d == 0:
            r.add(d)

print(len(r))