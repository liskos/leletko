import sys
sys.stdin=open("26.txt")
k = int(input())
n = int(input())
a = []
t = [[0] for _ in range(k)]
zareg6 = []
for _ in range(n):
    t1,t2 = map(int, input().split())
    a.append([t1,t2])
a = sorted(a, key=lambda x:x[0])
for t1, t2 in a:
    for i in range(k):#номер такси
        if t[i][-1] <= t1:
            t[i].append(t2)
            if 7200 <= t1 <= 8640:
                zareg6.append(i)
            break
print(a)
print(*t, sep="\n")
print(len(zareg6), zareg6[-1]+1)