file = open("26data/26-s1.txt")
n = int(file.readline())
a = [int(x) for x in file]
h = []
c = [x for x in a if x > 100]
a = [x for x in a if x not in c]
c.sort()
print(c[len(c)//2-1])
for x in range(len(c)//2):
    sk = c[x]/10*9
    h.append(sk)
    c[x] = 0
print(sum(a) +sum(c)+int(sum(h))+1)