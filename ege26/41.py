file = open("26data/26-j10.txt")
vd, ve, n = map(int,file.readline().split())
a = [int(x) for x in file]
d = sorted([int(x) for x in a if int(x) > 500])
e = sorted([int(x) for x in a if int(x) < 500])
d_end = []
while sum(d_end) + d[0] <= vd:
    d_end.append(d.pop(0))
d1 = d_end[:-1] + [max([x for x in d if sum(d_end[:-1]) + x <= vd and x not in d_end])]
e_end = []
while sum(e_end) + e[0] <= ve:
    e_end.append(e.pop(0))
e1 = e_end[:-1] + [max([x for x in e if sum(e_end[:-1]) + x <= ve and x not in e_end])]

print(len(d1) + len(e1), max(d1) + max(e1))
