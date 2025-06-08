file = open("26data/26-k6.txt")
n,k = map(int,file.readline().split())
a = []
for _ in range(n):
    ves, stoim = map(int, file.readline().split())
    a.append([ves, stoim, stoim/ves]) # вес, цена, цена за кг
a.sort(key=lambda x:(x[2], -x[0]))
print(a)
v = a[:k]
print("суммарный вес пакетов", sum(i for i,j,k in v))
v.sort(key=lambda x:x[0], reverse=True)
print("стоимость самого тяжелого отправленного пакета", v[0][1])

