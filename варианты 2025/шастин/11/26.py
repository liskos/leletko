def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [[0, 0]] + [list(map(int, file.readline().split())) for _ in range(n)] + [[86_400_001, 86_400_001]]
    a.sort(key=lambda x:(x[0], x[1]))
    print(f"кол-во приёмов {n}")
    print(f"приёмы {a[:20]}")
    t_end = a[0][1]
    k = 0
    sum_pr = 0
    for t1, t2 in a:
        if t1 - t_end > 1:
            k += 1
            sum_pr += t1 - t_end - 1
        t_end = max(t2, t_end)
    return k, sum_pr


print(*f("26test.txt"))
print(*f("26.txt"))