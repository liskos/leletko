a = [int(x) for x in open("17.txt")]
m = max([x for x in a])
r = []
for i in range(1, len(a)):
    if (i + i + 1) % 10 == int(str(m)[-1]):
        b = abs((a[i] + a[i+1]) - (i + i +1))
        r.append(b)

print(len(r), min(r))