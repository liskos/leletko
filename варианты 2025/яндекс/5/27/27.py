def number_nedeli(a):
    m, d, g = map(int, a)
    data = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    s = sum(data[:m])+d
    return (s+6)//7


a = [line.split("\t")  for line in open("27_A.txt", encoding="utf-8")]
b = []
c = [[0, 0] for _ in range(100)]
for i in range(len(a)):
    a[i][0] = int(a[i][0])
    a[i][1] = int(a[i][1])
    a[i][4] = a[i][4].split()[0].split("/")
    a[i][5] = int(a[i][5])
    a[i][6] = a[i][6][:-1]
    if a[i][3] == "Да" and a[i][5] >= 5:
        b.append(a[i]+[number_nedeli(a[i][4])])
print(*b, sep="\n")
for i in b:
    if i[2] == "Подарки на новый год":
        c[i[7]][0] += 1
    if i[2] == "Образование":
        c[i[7]][1] += 1
for i in range(100):
    if c[i][0] > c[i][1]:
        print(i, *c[i])
# 43 - 53 неделя
d = [0] * 1000
for i in b:
    if i[2] == "Образование" and 43 <= i[7] <= 53:
        d[i[1]] += 1
print(max(d))
# 1A) 9
e = 0
for i in b:
    if i[2] == "Образование" and 43 <= i[7] <= 53 and i[6]=="13-17":
        e += 1
print(e)
# A) 9 26

a = [line.split("\t")  for line in open("27_B.txt", encoding="utf-8")]
b = []
c = [[0, 0] for _ in range(100)]
for i in range(len(a)):
    a[i][0] = int(a[i][0])
    a[i][1] = int(a[i][1])
    a[i][4] = a[i][4].split()[0].split("/")
    a[i][5] = int(a[i][5])
    a[i][6] = a[i][6][:-1]
    if a[i][3] == "Да" and a[i][5] >= 5:
        b.append(a[i]+[number_nedeli(a[i][4])])
print(*b, sep="\n")
for i in b:
    if i[2] == "Образование":
        c[i[7]][0] += 1
    if i[2] == "Путешествия" or i[2] == "Электроника"  :
        c[i[7]][1] += 1
for i in range(100):
    if c[i][0] > c[i][1]:
        print(i, *c[i])
# 8- 22 неделя
d = [0] * 1000
for i in b:
    if i[2] == "Образование" and 8 <= i[7] <= 22:
        d[i[1]] += 1
print(max(d))
# 1Б) 82
e = 0
for i in b:
    if i[2] == "Образование" and 8 <= i[7] <= 22 and i[6]=="13-17":
        e += 1
print(e)
# Б) 82 333