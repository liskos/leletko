file = open("26data/26-42.txt")
n,s = map(int,file.readline().split())
a = []
for i in range(n):
    h,j,g = file.readline().split()
    a.append([h,int(j), int(g)])
a = sorted(a, key=lambda x: (x[0], x[1]))
print(a)
summ = [a.pop(0)]
while sum([x[1] * x[2] for x in summ]) + a[0][1]*a[0][2] <= s:
    summ.append(a.pop(0))
while sum(i[1]*i[2] for i in summ)+a[0][1] < s:
        summ.append([a[0][0], a[0][1], 1])

ka = [x[2] for x in summ if x[0] == "Z"]
vsumm = [x[1]*x[2] for x in summ]
print(s-sum(vsumm))
print(sum(ka))