import math
#1071 26
file = open("27B.txt")
n, k = map(int,file.readline().split())
data = [list(map(float,file.readline().split())) for _ in range(n)]
zapret = [list(map(float,file.readline().split())) for _ in range(k)]
print(len(data), "все")
for p1 in zapret:
    for p2 in data.copy():
        if math.dist(p1,p2) <= 5:
            data.remove(p2)
print(len(data), "разрешенные")

m = []
for p1 in data:
     m += [(len([p2 for p2 in data if math.dist(p1,p2) <= 7]),p1)]


mm = max(m, key=lambda x:(x[0], x[1][0]+x[1][1]))
x, y = mm[1]
print([x for x in m if x[0] == mm[0]])
print(x * 10**9, y * 10**9)