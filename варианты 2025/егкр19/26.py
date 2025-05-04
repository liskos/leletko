def max_od(a):
    """функция находит максимальное количество через одну"""
    a = sorted(a)
    chet = [x for x in a if x % 2 == 0]
    m = 1
    k = 1
    for i in range(1, len(chet)):
        if chet[i] - 2 == chet[i-1]:
            k += 1
            m = max(m, k)
        else:
            k = 1
    nechet = [x for x in a if x % 2 == 1]
    k = 1
    for i in range(1, len(nechet)):
        if nechet[i] - 2 == nechet[i-1]:
            k += 1
            m = max(m, k)
        else:
            k = 1
    return m


def f(filename):
    file = open(filename)
    n = int(file.readline())
    print(f"кол-во зачтенных решений {n}")
    dict_stydent = dict()
    for _ in range(n):
        id,nzadahi = map(int,file.readline().split())
        dict_stydent[id] = dict_stydent.get(id, set()) | {nzadahi}
    #print(f"словарь решенных студентами задач", dict_stydent)
    m = [[id , max_od(dict_stydent[id])] for id in dict_stydent]
    m.sort(key=lambda x: (x[1],-x[0]), reverse=True)
    return m[0]

print(*f("26test.txt"))
print(*f("26_21719.txt"))