def f(file_name):
    file = open(file_name)
    n,m = map(int,file.readline().split())
    print(f"кол-во грузов {n}")
    print(f"вместимость {m}")
    a = [int(file.readline()) for _ in range(n)]
    #print(f"грузы {a}")
    a_pri = []
    a_ost = []
    for x in a:
        if 310 <= x <= 320:
            a_pri.append(x)
        else:
            a_ost.append(x)
    a_pri.sort(reverse=True)
    a_ost.sort()
    print(f"приоритетные грузы от 310 до 320: {a_pri}")
    print(f"остальные грузы: {a_ost}")
    v = a_pri.copy()
    print(f"погружено {sum(v)}, осталось места {m-sum(v)}")
    for x in a_ost:
        if x <= m - sum(v):
            v.append(x)
        else:break
    print(f"погружены {v}")
    print(f"осталось места {m - sum(v)}")
    return len(v), sum(v) + 8
print(f("26data/26-39.txt"))