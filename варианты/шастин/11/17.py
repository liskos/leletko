a = [int(x) for x in open("17.txt")]
m = max([x for x in a if len(str(abs(x))) == 4 and str(x)[-2:] == '22'])
z = []
for i in range(len(a) - 2):
    t = a[i:i + 3]
    if len({len(str(abs(t[0]))), len(str(abs(t[1]))), len(str(abs(t[2])))}) == 3 and sum(t) >= m:
       z.append(sum(t))
print(len(z), max(z))
print(m)