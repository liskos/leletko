def func(filename):
    f = open(filename)
    n = int(f.readline())
    s = dict()
    for _ in range(n):
        t,id,zad = f.readline().split()
        data, time = t.split("T")
        gggg, mm, dd = data.split("-")
        hh, minut, ss = time.split(":")
        t = int(ss) + int(minut) * 60 + int(hh) * 3600 + int(dd) * 24 * 3600
        s[id] = s.get(id, []) + [[zad, t]]
    m = max([len(s[i]) for i in s])
    b = [x for x in s if len(s[x]) == m]
    c = []
    for i in b:
        mmmm = max([t for zad, t in  s[i]])
        c.append([mmmm, i])
    return m, min(c)[1]



print(*func("26.txt"))
print("-------------")
print(*func("26t.txt"))
