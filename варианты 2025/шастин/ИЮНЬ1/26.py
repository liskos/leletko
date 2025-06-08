def mint(t):
    m = 10**10
    for i in range(len(t)-1):
        m = min(m,t[i+1]-t[i])
    return m

file = open("26_22605.txt")
n = int(file.readline())
a = [list(map(int,file.readline().split())) for _ in range(n)]
a.sort()
b = [[0, 0, []]]
for x,y,t in a:
    if b[-1][0] == x and b[-1][1] == y:
        b[-1][2].append(t)
    else:
        b.append([x,y,[t]])
c = [[x[0]+x[1],mint(x[2])] for x in b if len(x[2]) >= 2]

c.sort(key=lambda x: x[1])
print(c[:10])
