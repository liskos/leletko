a = [int(x) for x in open("17data/17-297.txt")]
c = []
m = max([x for x in a if x % 51 == 0])
s = [int(str(x)[-1]) for x in a]
for i in range(len(a)- 1):
    if (a[i] == s[i] * 51 and a[i+1] != s[i+1] * 51) or (a[i] != s[i] * 51 and a[i+1] == s[i+1] * 51):
        if a[i] + a[i+1] < m:
            c.append(a[i]+a[i+1])
print(len(c), max(c))