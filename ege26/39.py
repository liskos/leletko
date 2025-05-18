def f(file_name):
    file = open(file_name)
    n,m = map(int,file.readline().split())
    print(f"кол-во грузов {n}")
    print(f"вместимость {m}")
    a = [int(file.readline()) for _ in range(n)]
    a_pri = []
    a_ost = []
    for x in a:
        if 180 <= x <= 200:
            a_pri.append(x)
        else:
            a_ost.append(x)
    a_pri.sort(reverse=True)
    a_ost.sort()
    print(f"приоритетные грузы от 180 до 200: {a_pri}")
    print(f"остальные грузы: {a_ost}")
    v = a_pri.copy()
    print(f"погружено {sum(v)}, осталось места {m-sum(v)}")
    kd = 0
    for x in a_ost:
        if x <= m - sum(v):
            v.append(x)
            kd += 1
        else:break
    print(f"погружены {v}")
    print(f"осталось места {m - sum(v)}")
    posled = max([x for x in a_ost[kd:] if x + sum(v[:-1]) <= m])
    return len(v), sum(v[:-1]) + posled

print(f("26data/26-39.txt"))