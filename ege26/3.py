file = open("26data/26-3.txt")
s,n = map(int,file.readline().split())
print(f"объём {s}")
print(f"кол-во объёмов {n}")
a = [int(x) for x in file]
a.sort()
print(f"все объёмы{a}")
b = []
while sum(b) + a[0] <= s:
    b.append(a.pop(0))
print(f"число объёмов {len(b)}")
a.append(b.pop(-1))
m = [x for x in a if sum(b) + x <= s]
print(f"макс объём {max(m)}")

