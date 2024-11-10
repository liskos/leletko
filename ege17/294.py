def k(n):
    return (int(n ** 0.5)) ** 2 == n

def s(n):
    s = 0
    while n > 0:
        s = s + n%10
        n = n // 10
    return s


a = [int(x) for x in open("17data/17-294.txt")]
c = []
sr = sum(a) / len(a)
for i in range(len(a)- 1):
    if k(s(a[i])+s(a[i+1])) and a[i] + a[i+1] > sr:
        c.append(s(a[i]) + s(a[i+1]))
print(len(c), max(c))