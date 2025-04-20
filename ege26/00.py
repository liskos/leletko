file = open("26data/26.txt")
s,n = map(int,file.readline().split())
print(f"свободный объём {s}")
print(f"число файлов {n}")
a = [int(file.readline()) for _ in range(n)]
a.sort()
b = [] # файлы для сохранения
print(f"объёмы {a}")
while sum(b) + a[0] <= s:
    b.append(a.pop(0))
print(f"макс число пользователей {len(b)}")
a.append(b.pop(-1))
m = [x for x in a if sum(b) + x <= s]
print(f"макс файл сохр {max(m)}")