a = [int(x) for x in open("17.txt")]
r = []
k = 0
m = max(a)
for i in range(len(a) - 1):
    if str(i + i + 1 + 2)[-1] == str(m)[-1]:
        d = abs((a[i] + a[i+1]) - (i + i + 1 + 2))
        r.append(d)
print(len(r), min(r))