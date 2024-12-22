def f(s):
    import sys
    sys.stdin = open(s)
    n = int(input())
    time = [[] for i in range(24*60)]
    for i in range(n):
        number,t1,t2 = map(int,input().split())
        for j in range(t1,t2):
            time[j].append(number)
    kol = [len(x) for x in time]
    m = max(kol)
    a = []
    f = False
    for i in range(len(time)):
        if kol[i] == m and not f:
            a.append([i])
            f = True
        elif kol[i] == m and f and i+1 < 24*60 and kol[i+1] != m:
            a[-1].append(i)
            f = False
    b = [x[1] - x[0] for x in a]
    minuta1 = a[b.index(max(b))][0]
    minuta2 = a[b.index(max(b))][1]
    ss = set()
    for minuta in range(minuta1, minuta2+1):
        ss |= set(time[minuta])
    return len(a), sum(ss)

if __name__ == "__main__":
    print(*f("26.txt"))