file = open("26data/26-58.txt")
s,n = map(int,file.readline().split())
print(s,n)
a = [int(file.readline()) for _ in range(n)]
a.sort()
b = [x for x in a if a.count(x) > 1 ]
print("все парные и более ", b)
c = []
for x in b:
    if x + sum(c) <= s:
        c.append(x)
    else:
        break
print("выбранные ", c)
print("сумма выбранных ", sum(c), "оставшееся место", s- sum(c))
k1 = (44 + 44 + 43) /2
m1 = max([x for x in b if x <= k1])
print("1 ответ", m1)
c = c[:-2] + [64, 64]
m2 = max([c.count(x) for x in c])
print(m2)