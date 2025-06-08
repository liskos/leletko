file = open("26.txt")
n,k = map(int,file.readline().split())
print(f"кол-во устр {n}")
print(f"кол-во мастер {k}")
a = [list(map(int,file.readline().split())) for _ in range(n)]
a.sort()
mast = [[0] for _ in range(k)]
ytil = []
print(a)
for t1, t, n_mastr in a:
    if n_mastr != 0:
        och = mast[n_mastr-1]
        koli_och = len([x for x in och if x > t1])
        if koli_och < 5:
            mast[n_mastr-1].append(max(och[-1], t1) +t)
        # определяем в конкретную мастерскую
        # если в очередях 5 или более устройств включая ремонтируемое то на утилизацию
        else:
            ytil.append([t1, t, n_mastr])
    else:
        # определяем в мастерскую с наименьшей очередью, если таких несколько , то с наименьшим номером
        # если в очередях 5 или более устройств включая ремонтируемое то на утилизацию
        kol_ocher = []
        for i in range(k):
            och = mast[i]
            kol_ocher.append(len([x for x in och if x > t1]))
        min_mast = min(kol_ocher)
        if min_mast < 5:
            ind = kol_ocher.index(min_mast)
            mast[ind].append(max(mast[ind][-1], t1) + t)
        else:
            ytil.append([t1, t, n_mastr])

print(max([len(x)-1 for x in mast]), len(ytil))