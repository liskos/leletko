file = open("26data/26-1.txt")
s,n = map(int,file.readline().split())
print(f"место {s}")
print(f"кол-во файлов {n}")
a = [int(x) for x in file]
a.sort()
print(f"объёмы {a}")
b = []
while sum(b) + a[0] <= s:
    b.append(a.pop(0))
print(f"макс кол-во сохр {len(b)}")
a.append(b.pop(-1))
m = [x for x in a if sum(b) + x <= s]
print(f"макс сох файл {max(m)}")